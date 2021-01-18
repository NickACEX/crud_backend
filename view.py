class Menu_View:

    def __init__(self,menu_options,title="CRUD"):
        self.__menu_options = menu_options

        lbl_title = "\t"*4+title
        underline = "\t"*4+"-"*len(title)
        print(lbl_title)
        print(underline)
        print()

        for i in range(len(tuple(self.__menu_options.keys()))):
            print(f"{i+1}. {tuple(self.__menu_options.keys())[i]}")

    def ask_option(self,mss_option="Ingrese Opción"):
        option_number = input(mss_option+": ").strip()
        if option_number not in [str(i+1) for i in range(len(self.__menu_options))]:
            print("Incorrect Option")
        else:
            self.__execute_option(int(option_number)-1)

    def __execute_option(self,option):
        try:
            key = tuple(self.__menu_options.keys())[option]
            self.__menu_options[key]()#execute action 
        except TypeError as error:
            print(str(error))


def separator(data,list_high):
    print()
    for i in data:
        print("-"*(list_high[i]+2),end="")
    print()

def print_table(data):
    list_high = {}
    number_row = 0
    for i in data:
        size_data = len(data[i])
        if number_row < size_data:
            number_row = size_data
        high = len(i) 
        for j in data[i]:
            size_element = len(str(j))
            if high < size_element:
                high = size_element
        list_high[i] = high
    print()
    for i in data:#print title
        print(i.title(),end=" "*(list_high[i]-len(i)+1)+"|")
    
    separator(data,list_high)

    index = 0
    while index < number_row:
        for i in data:
            if index >= len(data[i]):
                data[i].append("")
            element = data[i][index]
            print(element,end = " "*(list_high[i]-len(str(element))+1)+'|')
        separator(data,list_high)
        index += 1

