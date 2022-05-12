KV = """
<MenuScreen>:
    BoxLayout:
        orientation: 'horizontal'
        BoxLayout:
            orientation:'vertical'
            Button:
                text:'Base'
                background_color: .78,.57,.87,.6
                on_press:
                    root.manager.current = 'base'

            Button:
                text:'Add'
                background_color: .78,.57,.87,.8
                on_press: root.manager.current = 'add'
            Button:
                text:'Search'
                background_color: .78,.57,.87,.8
                on_press: root.manager.current = 'search'
            Button:
                text:'Delete'
                background_color: .78,.57,.87,.8
                on_press: root.manager.current = 'delete' 
            Button:
                text:'Upload'
                background_color: .78,.57,.87,.6
                on_press: root.manager.current = 'upload'


<BaseScreen>:
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation:'horizontal'                   
            Button:
                text: 'Menu'
                size_hint: .2,1
                background_color: .78,.57,.87,.8
                on_press: 
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'     
            GridLayout:
                spacing:10
                rows:2
                cols:5
                Label:
                    text:'Full name'
                    color: 0,0,0,1
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size 
                Label:
                    text:'Group'
                    color: 0,0,0,1    
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size   
                Label:
                    text:'V/R'
                    color: 0,0,0,1
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size  
                Label:
                    text:'Inv/R'
                    color: 0,0,0,1
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size 
                Label:
                    text:'Total'
                    color: 0,0,0,1 
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size
                Label:
                    id:full_name_base_id
                    text:''
                    color: 0,0,0,1 
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size    
                Label:
                    id:group_base_id
                    text:''
                    color: 0,0,0,1   
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size         
                Label:
                    id:valid_reason_base_id
                    text:''
                    color: 0,0,0,1
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size
                Label:
                    id:invalid_reason_base_id
                    text:''
                    color: 0,0,0,1 
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size 
                Label:
                    id:totall_base_id
                    text:''
                    color: 0,0,0,1  
                    size_hint_x:None
                    size_hint_y:None
                    size: self.texture_size                                                                  
            Button:
                text: 'Update'
                size_hint: .2,1
                background_color: .78,.57,.87,.8
                on_press: root.update() 
            
            
        BoxLayout:
            size_hint: 1,.1
            orientation:'horizontal'   
            Button:
                text: 'Previos'
                background_color: .62,.48,.63,1
                on_press: root.update(-1)
            Button:
                text: 'Next'
                background_color: .62,.48,.63,1
                on_press: root.update(1)
            Button:
                text: 'Update'
                background_color: .62,.48,.63,1
                on_press: root.change_number_of_strings(number_of_strings.text)
            TextInput:
                id:number_of_strings
                hint_text:'strings on page'          
                

<AddScreen>:
    BoxLayout:                   
        Button:
            text: 'Back'
            background_color: .78,.57,.87,.8
            on_press: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
            size_hint: .1,1
        BoxLayout:
            padding:50
            spacing:20
            orientation: 'vertical'
            TextInput:
                id:full_name
                hint_text:'Full name'
            TextInput:
                id:group
                hint_text:'Group'
            TextInput:
                id:valid_reason
                hint_text:'Valid reason'
            TextInput:
                id:invalid_reason
                hint_text:'Invalid reason'
            Button:
                on_press: root.input_validation(full_name.text,group.text,valid_reason.text,invalid_reason.text)
                text: 'Done'
                background_color: .78,.57,.87,.8

<SearchScreen>:
    BoxLayout:                   
        Button:
            text: 'Back'
            background_color: .78,.57,.87,.8
            on_press: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
            size_hint: .1,1
        BoxLayout:
            padding:50
            spacing:20
            orientation: 'vertical'
            TextInput:
                id:full_name
                hint_text:'Full name'
            TextInput:
                id:group
                hint_text:'Group'
            TextInput:
                id:valid_reason
                hint_text:'Valid reason'
            TextInput:
                id:invalid_reason
                hint_text:'Invalid reason'
            Button:
                on_press: root.find(full_name.text,group.text,valid_reason.text,invalid_reason.text)
                text: 'Search'
                background_color: .78,.57,.87,.8
            ScrollView:
                do_scroll_x: False
                do_scroll_y: True
            
                Label:
                    id:search_label_id
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: 5, 5
                    text: ''
                    color: 0,0,0,1
<DeleteScreen>:
    BoxLayout:                   
        Button:
            text: 'Back'
            background_color: .78,.57,.87,.8
            on_press: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
            size_hint: .1,1
        BoxLayout:
            padding:50
            spacing:20
            orientation: 'vertical'
            TextInput:
                id: full_name
                hint_text:'Full name'
            TextInput:
                id: group
                hint_text:'Group'
            TextInput:
                id: valid_reason
                hint_text:'Valid reason'
            TextInput:
                id: invalid_reason
                hint_text:'Invalid reason'
            Button:
                on_press: 
                    root.delete(full_name.text,group.text,valid_reason.text,invalid_reason.text)
                text: 'Delete'
                background_color: .78,.57,.87,.8
            ScrollView:
                do_scroll_x: False
                do_scroll_y: True
            
                Label:
                    id:delete_label_id
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: 5, 5
                    text: ''
                    color: 0,0,0,1
<UploadScreen>
    BoxLayout:
        orientation:'horizontal'                
    TextInput:
        id:file
        hint_text:'File path' 
    Button:
        text: 'Done'
        size_hint: 1,.1
        background_color: .78,.57,.87,.8
        on_press:
            root.upload_file(file.text)
            root.manager.transition.direction = 'right'
"""
