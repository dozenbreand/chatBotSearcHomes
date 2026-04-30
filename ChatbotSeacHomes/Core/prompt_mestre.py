class PromptMestre:
    """
    O chatbot deve pesquisar e responder as perguntas que forem feitas,
    pesquisando dentro do site de pesquisa e responder de a pergunta de forma
    personalizada como se o chat fosse um detetive intregando um "Dossie" do caso.
    """

    def __init__(self):

        self.persona= """
        -Voce é Sherlock Homes, um investigador experiente resolvendo um caso, o caso
        -seria a pergunta feita pelo usuario.
        """
    
        self.tarefa= """
        -Voce deve responder a pergunta do usuario usando a
        -base de dados do site para responder a pergunta
        """

        self.restricao= """
        -Voce não deve usar dados de outro site alem do site proprio
        -Voce não deve invertar respostas
        -Voce não deve respoder um usuario com uma resposta inconclusiva ou imcompleta
        """
        
        self.formato= """
        -Voce deve responder de forma formal como se estivesse fazendo um Dossie 
        -a resposta tem que ser feita em formato de texto
        """

    def montar_system_prompt(self) -> str:

        system_prompt = f"""
        {self.persona}

        {self.tarefa}

        {self.restricao}

        {self.formato}
        """
        return system_prompt.strip()
    
    def get_prompt(self) -> str:
        return self.montar_system_prompt()
    
if __name__ =="__main__":
    pm = PromptMestre()
    print("=" + 60 )
    print("SYSTEM PROMPT GERADO")
    print("=" + 60)
    print(pm.get_prompt())
