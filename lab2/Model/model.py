import read
import write

import os.path
import math


class Model:
    curr_page = 0
    information = {'full_name': [], 'group': [], 'valid_reason': [], 'invalid_reason': [], 'totall': []}
    number_of_strings=10

    def file_name_validation(self, file_name):
        return os.path.exists(file_name)

    def upload_file(self, file_name):
        file_name = f"file_xml/{file_name}"
        handler = read.Reader()
        handler.parser.setContentHandler(handler)
        handler.parser.parse(file_name)

        self.information['full_name'] = handler.student_full_name
        self.information['group'] = handler.student_group
        self.information['valid_reason'] = [int(x) for x in handler.student_valid_reason]
        self.information['invalid_reason'] = [int(x) for x in handler.student_invalid_reason]
        self.information['totall'] = list(
            map(sum, zip(Model.information['valid_reason'], Model.information['invalid_reason'])))

    def save_file(self, file_name):
        write.make_xml(self.information).writexml(open(file_name, 'w', encoding='utf-8'),
                                                  indent="   ",
                                                  addindent="    ",
                                                  newl='\n'
                                                  )

    def update(self, navigation):
        if navigation == -1:
            self.curr_page -= 1
        elif navigation == 1:
            self.curr_page += 1
        return self.next_page(self)
    def change_number_of_strings(self,number_of_strings):
        if number_of_strings.isdigit():
            self.number_of_strings=int(number_of_strings)
        else:
            pass

    def next_page(self):
        information = []
        full_name=''
        group=''
        valid_reason=''
        invalid_reason=''
        totall=''
        start = self.curr_page * self.number_of_strings
        for i in range(start, start + self.number_of_strings):
            if self.curr_page>=math.ceil(len(Model.information['full_name'])/self.number_of_strings):
                self.curr_page = math.ceil(len(Model.information['full_name'])/self.number_of_strings)
                break
            if self.curr_page <=-1:
                self.curr_page =-1
                break
            if len(Model.information['full_name']) <= i:
                break
            elif start < 0:
                self.curr_page = 1
                break
            else:
                full_name+=f"{i + 1}){Model.information['full_name'][i]}\n"
                group+=f"| {Model.information['group'][i]} |\n"
                valid_reason+=f"{Model.information['valid_reason'][i]}\n"
                invalid_reason+=f"{Model.information['invalid_reason'][i]}\n"
                totall+=f"{Model.information['totall'][i]}\n"
        information.append(full_name)
        information.append(group)
        information.append(valid_reason)
        information.append(invalid_reason)
        information.append(totall)
        return information

    def add(self, full_name, group, valid_reason, invalid_reason):
        Model.information['full_name'].append(full_name)
        Model.information['group'].append(group)
        Model.information['valid_reason'].append(int(valid_reason))
        Model.information['invalid_reason'].append(int(invalid_reason))
        Model.information['totall'].append(int(valid_reason) + int(invalid_reason))

    def searching(self, full_name, group, valid_reason, invalid_reason):
        list_of_index = []
        if full_name != '':
            list_of_index = [i for i in range(len(Model.information['full_name'])) if
                             full_name.lower() in Model.information['full_name'][i].lower()]
        elif group != '':
            list_of_index = [i for i in range(len(Model.information['group'])) if
                             group in Model.information['group'][i]]
        elif valid_reason != '':
            list_of_index = [i for i in range(len(Model.information['valid_reason'])) if
                             int(valid_reason) == Model.information['valid_reason'][i]]
        elif invalid_reason != '':
            list_of_index = [i for i in range(len(Model.information['invalid_reason'])) if
                             int(invalid_reason) == Model.information['invalid_reason'][i]]
        return list_of_index

    def find(self, list_of_index):
        found_string = ''.join([
            f"{Model.information['full_name'][index]} {Model.information['group'][index]} [{Model.information['valid_reason'][index]}, {Model.information['invalid_reason'][index]}] ({Model.information['totall'][index]}) \n"
            for index in list_of_index])
        return (found_string)

    def delete(self, list_of_index):
        delete_string = ''
        for index in reversed(list_of_index):
            delete_string += f"{Model.information['full_name'][index]} {Model.information['group'][index]} [{Model.information['valid_reason'][index]}, {Model.information['invalid_reason'][index]}] ({Model.information['totall'][index]}) \n"
            del Model.information['full_name'][index]
            del Model.information['group'][index]
            del Model.information['valid_reason'][index]
            del Model.information['invalid_reason'][index]
            del Model.information['totall'][index]
        return delete_string
