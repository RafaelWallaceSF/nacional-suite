import frappe

KNOWLEDGE_BASE = {
    "demissao": "### 📄 Como realizar a Demissão / Desligamento de um Funcionário:\n\n1. No menu lateral, acesse **Recursos Humanos** ➔ **Funcionários**.\n2. Clique no nome do funcionário que deseja desligar.\n3. No canto superior direito, clique em **Ações** ou vá até a seção **Desligamento**.\n4. Clique em **Criar Processo de Desligamento (Employee Separation)**.\n5. Preencha a **Data de Desligamento**, o **Motivo** e o **Status da Entrevista de Desligamento**.\n6. Clique no botão azul **Salvar** e depois em **Submeter**.",
    "vaga": "### 💼 Como criar uma Vaga de Emprego (Job Opening):\n\n1. No menu lateral, acesse **Recrutamento**.\n2. Clique no cartão **Vagas Abertas (Job Opening)**.\n3. Clique no botão azul **+ Nova Vaga Aberta** no canto superior direito.\n4. Selecione o **Cargo (Designation)**, o **Departamento** e a **Quantidade de Vagas**.\n5. Insira a descrição das responsabilidades e requisitos da vaga.\n6. Defina o status como **Aberta (Open)** e clique em **Salvar**.",
    "ferias": "### 🌴 Como solicitar ou lançar Férias / Licença:\n\n1. No menu lateral, acesse **Férias e Licenças**.\n2. Clique em **Solicitação de Férias/Licença (Leave Application)**.\n3. Clique em **+ Criar Solicitação**.\n4. Selecione o **Funcionário** e o **Tipo de Licença** (ex: Férias Regulamentares, Licença Médica).\n5. Escolha a **Data Inicial** e a **Data Final**.\n6. Clique em **Salvar** e depois em **Submeter** para enviar para aprovação.",
    "reembolso": "### 💳 Como solicitar Reembolso de Despesas (Expense Claim):\n\n1. No menu lateral, acesse **Reembolso de Despesas**.\n2. Clique em **+ Nova Solicitação de Reembolso**.\n3. Selecione o **Funcionário** e a **Categoria da Despesa** (ex: Viagem, Alimentação, Combustível).\n4. Digite o **Valor** e anexe o comprovante/recibo.\n5. Clique em **Salvar** e **Submeter** para a equipe financeira aprovar.",
    "folha": "### 💰 Como processar a Folha de Pagamento:\n\n1. No menu lateral, acesse **Folha de Pagamento**.\n2. Clique em **Processamento da Folha (Payroll Entry)**.\n3. Clique em **+ Novo Processamento**.\n4. Escolha a **Empresa**, o **Período da Folha** (Mês/Ano) e o **Departamento**.\n5. Clique em **Obter Funcionários** e depois em **Gerar Holerites**.\n6. Após conferir os valores, clique em **Submeter Folha**."
}

@frappe.whitelist(allow_guest=True)
def ask_ai(question=None, current_route=None):
    if not question:
        return {"reply": "Olá! Sou o Assistente Virtual do **Nacional Suite**. Como posso ajudar você hoje?"}

    q_clean = question.lower().strip()

    if any(k in q_clean for k in ["demit", "deslig", "demis", "sair", "demissao"]):
        return {"reply": KNOWLEDGE_BASE["demissao"]}
    elif any(k in q_clean for k in ["vaga", "recrut", "contrat", "candidat"]):
        return {"reply": KNOWLEDGE_BASE["vaga"]}
    elif any(k in q_clean for k in ["feria", "licen", "folga", "ausen"]):
        return {"reply": KNOWLEDGE_BASE["ferias"]}
    elif any(k in q_clean for k in ["reembols", "despes", "gasto", "comprov"]):
        return {"reply": KNOWLEDGE_BASE["reembolso"]}
    elif any(k in q_clean for k in ["folha", "salari", "holerit", "pagament"]):
        return {"reply": KNOWLEDGE_BASE["folha"]}

    return {
        "reply": f"### 💡 Orientações no Nacional Suite\n\nPara a sua dúvida: *\"{question}\"*\n\n1. Utilize a barra de pesquisa rápida no topo do sistema (**Ctrl + K**).\n2. Digite o nome do módulo ou formulário desejado.\n3. Caso precise de um passo a passo específico, você pode me perguntar sobre:\n   - *Como demitir um funcionário?*\n   - *Como criar uma vaga de emprego?*\n   - *Como solicitar férias?*\n   - *Como lançar reembolso de despesas?*\n   - *Como processar a folha de pagamento?*"
    }
