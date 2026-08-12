import frappe

APP_LOGO = "/assets/nacional_suite/images/suite-logo.png"
APP_NAME = "Nacional Suite"

MASSIVE_PT_TRANSLATIONS = {
    # Dashboards & Breadcrumbs & General Navigation
    "Leaves": "Férias e Licenças",
    "Leave": "Férias e Licenças",
    "Recruitment": "Recrutamento",
    "Performance": "Desempenho",
    "Payroll": "Folha de Pagamento",
    "HR": "Recursos Humanos",
    "Human Resource": "Recursos Humanos",
    "Human Resources": "Recursos Humanos",
    "Attendance": "Frequência e Ponto",
    "Shift": "Escala de Trabalho",
    "Shift Management": "Escala de Trabalho",
    "Expense": "Reembolso de Despesas",
    "Expense Claim": "Reembolso de Despesas",
    "Expense Claims": "Reembolso de Despesas",
    "Employees": "Funcionários",
    "Employee": "Funcionário",
    "Accounting": "Contabilidade",
    "Stock": "Estoque",
    "Buying": "Compras",
    "Selling": "Vendas",
    "CRM": "Gestão de Clientes",
    "Assets": "Ativos",
    "Projects": "Projetos",
    "Manufacturing": "Manufatura",
    "Quality": "Qualidade",
    "Integrations": "Integrações",
    "Settings": "Configurações",
    "Build": "Desenvolvimento",
    "Customization": "Personalização",
    "Tools": "Ferramentas",
    "Users": "Usuários e Permissões",
    "Website": "Website",
    "Core": "Núcleo",
    "Início": "Início",
    "Home": "Início",
    "Painel": "Painel",

    # Leaves & HR Specific
    "Leave Application": "Solicitação de Férias/Licença",
    "Leave Encashment": "Resgate de Licença",
    "Leave Control Panel": "Painel de Controle de Férias",
    "Leave Policy Assignment": "Atribuição de Política de Férias",
    "Leave Allocation": "Alocação de Férias",
    "Employees on leave today": "Funcionários de licença hoje",
    "Employees on leave this month": "Funcionários de licença este mês",
    "Holidays in this month": "Feriados este mês",
    "Holiday List": "Lista de Feriados",
    "Leave Type": "Tipo de Licença",
    "Leave Period": "Período de Licença",
    "Leave Policy": "Política de Férias",
    "Leave Block List": "Lista de Bloqueio de Licenças",
    "Employee Leave Balance": "Saldo de Licenças do Funcionário",
    "Employee Leave Balance Summary": "Resumo do Saldo de Licenças do Funcionário",
    "Employees working on a holiday": "Funcionários trabalhando em feriado",
    "Compensatory Leave Request": "Solicitação de Folga Compensatória",
    "Alocação": "Alocações",
    "Application": "Solicitações",
    "Masters & Reports": "Cadastros e Relatórios",
    "relatórios": "Relatórios",
    "Configuração": "Configurações",
    "Configurações": "Configurações",

    # Recruitment & Performance
    "Job Opening": "Vaga Aberta",
    "Job Openings": "Vagas Abertas",
    "Job Applicant": "Candidato",
    "Job Applicants": "Candidatos",
    "Job Offer": "Proposta de Emprego",
    "Interview": "Entrevista",
    "Interview Feedback": "Feedback da Entrevista",
    "Appraisal": "Avaliação de Desempenho",
    "Appraisal Template": "Modelo de Avaliação",

    # Attendance & Shift
    "Attendance Request": "Solicitação de Ajuste de Ponto",
    "Shift Type": "Tipo de Turno",
    "Shift Assignment": "Atribuição de Turno",
    "Shift Request": "Solicitação de Troca de Turno",
    "Employee Checkin": "Registro de Ponto do Funcionário",

    # Payroll & Expense
    "Salary Slip": "Holerite / Contracheque",
    "Salary Structure": "Estrutura Salarial",
    "Payroll Entry": "Processamento da Folha",
    "Salary Component": "Componente Salarial",
    "Expense Claim Type": "Tipo de Reembolso",

    # Number Cards
    "Total Employees": "Total de Funcionários",
    "New Hires (This Year)": "Novas Contratações (Este Ano)",
    "Employee Exits (This Year)": "Desligamentos (Este Ano)",
    "Employees Joining (This Quarter)": "Entradas (Este Trimestre)",
    "Employees Relieving (This Quarter)": "Saídas (Este Trimestre)",
    "Total Salary Paid": "Total de Salários Pagos",
    "Pending Expense Claims": "Solicitações de Reembolso Pendentes",
    "Open Job Openings": "Vagas Abertas",
    "Total Applicants": "Total de Candidatos",
    "Total Leave Applications": "Total de Solicitações de Licença",
    "Employees On Leave Today": "Funcionários de Licença Hoje",

    # Dashboard Charts & Legends
    "Hiring vs Attrition Count": "Contratações vs Desligamentos",
    "Hiring Count": "Contratações",
    "Attrition Count": "Desligamentos",
    "Employees by Age": "Funcionários por Faixa Etária",
    "Employees by Gender": "Funcionários por Gênero",
    "Employees by Department": "Funcionários por Departamento",
    "Employees by Designation": "Funcionários por Cargo",
    "Employees by Branch": "Funcionários por Filial",
    "Monthly Salary Payout": "Pagamento Mensal de Salários",
    "Leave Applications by Type": "Solicitações de Licença por Tipo",
    "Attendance Status": "Status de Frequência",
    "Expense Claim Amount": "Valor de Reembolsos de Despesas"
}


def after_install():
    apply_branding()


def apply_branding():
    # 1. Navbar Settings
    try:
        frappe.db.set_single_value("Navbar Settings", "app_logo", APP_LOGO)
    except Exception:
        pass

    # 2. Website Settings
    for field, value in [
        ("app_name", APP_NAME),
        ("app_logo", APP_LOGO),
        ("splash_image", APP_LOGO),
        ("favicon", APP_LOGO),
        ("banner_html", f'<img src="{APP_LOGO}" style="max-height:32px; vertical-align:middle; margin-right:8px;" /> <span style="font-weight:600;font-size:16px;">{APP_NAME}</span>'),
        ("copyright", "Nacional Suite © 2026")
    ]:
        try:
            frappe.db.set_single_value("Website Settings", field, value)
        except Exception:
            pass

    # 3. System Settings & Language (pt-BR)
    try:
        frappe.db.set_single_value("System Settings", "app_name", APP_NAME)
        frappe.db.set_single_value("System Settings", "language", "pt-BR")
    except Exception:
        pass

    # 4. User Languages (pt-BR)
    try:
        frappe.db.sql("UPDATE `tabUser` SET language = 'pt-BR' WHERE language IS NULL OR language = '' OR language = 'en'")
    except Exception:
        pass

    # 5. Insert Translation Records in tabTranslation for pt-BR AND pt
    for source, target in MASSIVE_PT_TRANSLATIONS.items():
        for lang in ["pt-BR", "pt"]:
            try:
                exists = frappe.db.sql("SELECT name FROM `tabTranslation` WHERE source_text = %s AND language = %s", (source, lang))
                if not exists:
                    name = frappe.generate_hash(length=10)
                    frappe.db.sql(
                        "INSERT INTO `tabTranslation` (name, source_text, translated_text, language, creation, modified, owner, modified_by) VALUES (%s, %s, %s, %s, NOW(), NOW(), 'Administrator', 'Administrator')",
                        (name, source, target, lang)
                    )
                else:
                    frappe.db.sql(
                        "UPDATE `tabTranslation` SET translated_text = %s WHERE source_text = %s AND language = %s",
                        (target, source, lang)
                    )
            except Exception:
                pass

    # 6. Update tabNumber Card labels
    try:
        cards = frappe.db.sql("SELECT name, label FROM `tabNumber Card`", as_dict=True)
        for c in cards:
            if c["label"] in MASSIVE_PT_TRANSLATIONS:
                frappe.db.sql("UPDATE `tabNumber Card` SET label = %s WHERE name = %s", (MASSIVE_PT_TRANSLATIONS[c["label"]], c["name"]))
    except Exception:
        pass

    # 7. Update tabDashboard Chart names
    try:
        charts = frappe.db.sql("SELECT name, chart_name FROM `tabDashboard Chart`", as_dict=True)
        for c in charts:
            if c["chart_name"] in MASSIVE_PT_TRANSLATIONS:
                frappe.db.sql("UPDATE `tabDashboard Chart` SET chart_name = %s WHERE name = %s", (MASSIVE_PT_TRANSLATIONS[c["chart_name"]], c["name"]))
    except Exception:
        pass

    # 8. Update tabDashboard names
    try:
        dashboards = frappe.db.sql("SELECT name, dashboard_name FROM `tabDashboard`", as_dict=True)
        for d in dashboards:
            if d["dashboard_name"] in MASSIVE_PT_TRANSLATIONS:
                frappe.db.sql("UPDATE `tabDashboard` SET dashboard_name = %s WHERE name = %s", (MASSIVE_PT_TRANSLATIONS[d["dashboard_name"]], d["name"]))
    except Exception:
        pass

    # 9. Update tabWorkspace titles and JSON contents for ALL workspaces
    try:
        workspaces = frappe.db.sql("SELECT name, title, content, shortcuts, links FROM `tabWorkspace`", as_dict=True)
        for w in workspaces:
            new_title = MASSIVE_PT_TRANSLATIONS.get(w["title"], w["title"])
            if w["name"] in MASSIVE_PT_TRANSLATIONS:
                new_title = MASSIVE_PT_TRANSLATIONS[w["name"]]
                
            content_str = w.get("content") or ""
            shortcuts_str = w.get("shortcuts") or ""
            links_str = w.get("links") or ""
            
            for source, target in MASSIVE_PT_TRANSLATIONS.items():
                content_str = content_str.replace(source, target)
                shortcuts_str = shortcuts_str.replace(source, target)
                links_str = links_str.replace(source, target)

            frappe.db.sql(
                "UPDATE `tabWorkspace` SET title = %s, content = %s, shortcuts = %s, links = %s WHERE name = %s",
                (new_title, content_str, shortcuts_str, links_str, w["name"])
            )
    except Exception:
        pass

    # 10. Force App/Workspace title 'Suite' in Database
    try:
        frappe.db.sql("UPDATE `tabWorkspace` SET title = 'Suite' WHERE name = 'nacional_suite' OR title LIKE 'Nacional Su%' OR title = 'Nacional Suite'")
    except Exception:
        pass

    try:
        frappe.db.sql("UPDATE `tabDesktop Icon` SET label = 'Suite' WHERE module_name = 'nacional_suite' OR label LIKE 'Nacional Su%' OR label = 'Nacional Suite'")
    except Exception:
        pass

    try:
        frappe.db.sql("UPDATE `tabModule Def` SET custom_title = 'Suite' WHERE name = 'nacional_suite' OR module_name = 'nacional_suite'")
    except Exception:
        pass

    frappe.db.commit()
