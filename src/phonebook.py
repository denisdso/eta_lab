from collections import OrderedDict


class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        invalid_chars = ['#', '@', '!', '$', '%'] #Melhoria de codigo nos ifs

        for char in invalid_chars:
            if char in name:
                return 'Nome invalido'

        if len(number) == 0:
            return 'Numero invalido' #String invalida devia ser 'invalido'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        invalid_chars = ['#', '@', '!', '$', '%']  # Melhoria de codigo nos ifs

        for char in invalid_chars:
            if char in name:
                return 'Nome invalido'

        return self.entries[name]

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return list(self.entries.keys())

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
            else:
                return "Nenhum registro encontrado" #Melhoria no cod, caso não tenha registro.
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return self.entries

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return list(OrderedDict(sorted(self.entries.items(), key=lambda item: item[0], reverse=True)))

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'

    #Usado o TDD para adicionar método
    def change_number(self, name, new_number):
        """
        Altera o número associado a um nome existente na estrutura de dados.
        :param name: nome da pessoa em formato de string
        :param new_number: novo número da pessoa em formato de string
        :return: 'Nome não encontrado' ou 'Número alterado'
        """
        if name in self.entries:
            self.entries[name] = new_number
            return 'Número alterado'
        else:
            return 'Nome não encontrado'

    def get_name_by_number(self, number):
        """
        Obtém o nome associado a um número existente na estrutura de dados.
        :param number: número da pessoa em formato de string
        :return: nome associado ao número ou 'Número não encontrado'
        """
        for name, num in self.entries.items():
            if num == number:
                return name

        return 'Numero não encontrado'