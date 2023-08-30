from src.phonebook import Phonebook

class TestPhonebook:
    # Setup
    phonebook = Phonebook()

    nomeValido = "Maria"
    telefoneValido = "83998120668"
    nomeInvalidoComHastag = "#teste"
    nomeInvalidoComArroba = "@teste"
    nomeInvalidoComExlamacao = "!teste"
    nomeInvalidoComCifrao = "$teste"
    nomeInvalidoComPorcentagem = "%teste"
    resultadoNomeInvalido = "Nome invalido"
    numeroAdicionado = "Numero adicionado"
    numeroInvalido = "Numero invalido"
    numeroNaoEncontrado = "Numero não encontrado"
    nomeNaoEncontrado = 'Nome não encontrado'
    nenhumRegistroEncontrado = "Nenhum registro encontrado"
    limpandoPhoneBook = 'phonebook limpado'
    deletePhoneBook = 'Numero deletado'
    alterarPhoneBook = 'Número alterado'

    def test_add_phone_com_sucesso(self):
        # Chamada
        resultado = self.phonebook.add(self.nomeValido, self.telefoneValido)

        # Avaliação
        assert resultado == self.numeroAdicionado

    def test_add_phone_invalido_nome_com_hastag(self):
        # Chamada
        resultado = self.phonebook.add(self.nomeInvalidoComHastag, self.telefoneValido)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    def test_add_phone_invalido_nome_com_arroba(self):
        # Chamada
        resultado = self.phonebook.add(self.nomeInvalidoComArroba, self.telefoneValido)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    def test_add_phone_invalido_nome_com_exclamacao(self):
        # Chamada
        resultado = self.phonebook.add(self.nomeInvalidoComExlamacao, self.telefoneValido)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    def test_add_phone_invalido_nome_com_cifrao(self):
        # Chamada
        resultado = self.phonebook.add(self.nomeInvalidoComCifrao, self.telefoneValido)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    def test_add_phone_invalido_nome_com_porcentagem(self):
        # Chamada
        resultado = self.phonebook.add(self.nomeInvalidoComPorcentagem, self.telefoneValido)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    # Olhar com o professor
    def test_add_phone_sem_informar_numero(self):
        # Chamada
        resultado = self.phonebook.add(self.nomeValido, "")

        # Avaliação
        assert resultado == self.numeroInvalido

    def test_lookup_phone_invalido_nome_com_hastag(self):
        # Chamada
        resultado = self.phonebook.lookup(self.nomeInvalidoComHastag)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    def test_lookup_phone_invalido_nome_com_arroba(self):
        # Chamada
        resultado = self.phonebook.lookup(self.nomeInvalidoComArroba)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    def test_lookup_phone_invalido_nome_com_exlamacao(self):
        # Chamada
        resultado = self.phonebook.lookup(self.nomeInvalidoComExlamacao)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    def test_lookup_phone_invalido_nome_com_cifrao(self):
        # Chamada
        resultado = self.phonebook.lookup(self.nomeInvalidoComCifrao)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    def test_lookup_phone_invalido_nome_com_porcentagem(self):
        # Chamada
        resultado = self.phonebook.lookup(self.nomeInvalidoComPorcentagem)

        # Avaliação
        assert resultado == self.resultadoNomeInvalido

    def test_lookup_phone_com_sucesso(self):
        # Chamada
        self.phonebook.add(self.nomeValido, self.telefoneValido)
        resultado = self.phonebook.lookup(self.nomeValido)

        # Avaliação
        assert resultado == self.telefoneValido

    def test_get_names_com_registro(self):
        # Chamada
        self.phonebook.add(self.nomeValido, self.telefoneValido)
        resultado = self.phonebook.get_names()

        # Avaliação
        assert resultado == ['POLICIA', 'Maria']

    def test_get_numbers_com_registro(self):
        # Chamada
        self.phonebook.add(self.nomeValido, self.telefoneValido)
        resultado = self.phonebook.get_numbers()

        # Avaliação
        assert resultado == ['190', '83998120668']

    def test_clear_phonebook(self):
        # Chamada
        resultado = self.phonebook.clear()

        # Avaliação
        assert resultado == self.limpandoPhoneBook

    def test_search_phonebook(self):
        # Chamada
        self.phonebook.add(self.nomeValido, self.telefoneValido)
        self.phonebook.add(self.nomeValido, self.telefoneValido)
        resultado = self.phonebook.search(self.nomeValido)

        # Avaliação
        assert resultado == [{'83998120668', 'Maria'}]

    def test_search_phonebook_nao_encontrado(self):
        # Chamada
        resultado = self.phonebook.search("Luiza")

        # Avaliação
        assert resultado == self.nenhumRegistroEncontrado

    def test_get_phonebook_sorted(self):
        # Chamada
        self.phonebook.add("Maria", self.telefoneValido)
        self.phonebook.add("Denis", self.telefoneValido)
        self.phonebook.add("Amanda", self.telefoneValido)
        resultado = self.phonebook.get_phonebook_sorted()

        # Avaliação
        assert resultado == {'Amanda': '83998120668', 'Denis': '83998120668', 'Maria': '83998120668'}

    def test_get_phonebook_reverse(self):
        # Chamada
        self.phonebook.clear()
        self.phonebook.add("Amanda", self.telefoneValido)
        self.phonebook.add("Joao", self.telefoneValido)
        self.phonebook.add("Bianca", self.telefoneValido)
        resultado = self.phonebook.get_phonebook_reverse()

        # Avaliação
        assert resultado == ['Joao', 'Bianca', 'Amanda']

    def test_delete_phonebook(self):
        # Chamada
        self.phonebook.add(self.nomeValido, self.telefoneValido)
        resultado = self.phonebook.delete(self.nomeValido)

        # Avaliação
        assert resultado == self.deletePhoneBook

    # usado o TDD para aplicar metodo o metodo change_number depois
    def test_change_number_com_sucesso(self):
        # Chamada
        self.phonebook.add(self.nomeValido, self.telefoneValido)
        resultado = self.phonebook.change_number(self.nomeValido, "83998120654")

        # Avaliação
        assert resultado == self.alterarPhoneBook

    # usado o TDD para aplicar metodo o metodo change_number depois
    def test_change_number_nao_encontrado(self):
        # Chamada
        self.phonebook.clear()
        resultado = self.phonebook.change_number(self.nomeValido, self.telefoneValido)

        # Avaliação
        assert resultado == self.nomeNaoEncontrado

    # usado o TDD para aplicar metodo o metodo get_name_by_number depois
    def test_get_name_by_number(self):
        # Chamada
        self.phonebook.add(self.nomeValido, self.telefoneValido)
        resultado = self.phonebook.get_name_by_number(self.telefoneValido)

        # Avaliação
        assert resultado == self.nomeValido

    # usado o TDD para aplicar metodo o metodo get_name_by_number depois
    def test_get_name_by_number_nao_encontrado(self):
        # Chamada
        self.phonebook.clear()
        resultado = self.phonebook.get_name_by_number(self.telefoneValido)

        # Avaliação
        assert resultado == self.numeroNaoEncontrado

