/* Nacional Suite Comprehensive Translation & Branding Overrides (Portuguese Mode) */
var MASSIVE_PT_MAP = {
    // Dashboards & Breadcrumbs & Navigation
    "Human Resource": "Recursos Humanos",
    "Human Resources": "Recursos Humanos",
    "Payroll": "Folha de Pagamento",
    "Recruitment": "Recrutamento",
    "Performance": "Desempenho",
    "Leaves": "Férias e Licenças",
    "Attendance": "Frequência e Ponto",
    "Expense": "Reembolso de Despesas",
    "Expense Claims": "Reembolso de Despesas",
    "Shift": "Escala de Trabalho",
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
    "Settings": "Configurações",
    "Build": "Desenvolvimento",
    "Tools": "Ferramentas",

    // Number Cards
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

    # Dashboard Charts
    "Hiring vs Attrition Count": "Contratações vs Desligamentos",
    "Hiring Count": "Contratações",
    "Attrition Count": "Desligamentos",
    "Employees by Age": "Funcionários por Faixa Etária",
    "Employees by Gender": "Funcionários por Gênero",
    "Employees by Department": "Funcionários por Departamento",
    "Employees by Designation": "Funcionários por Cargo",
    "Employees by Branch": "Funcionários por Filial",

    // Workspaces & Links
    "Leave Application": "Solicitação de Férias/Licença",
    "Leave Encashment": "Resgate de Licença",
    "Leave Control Panel": "Painel de Controle de Férias",
    "Leave Policy Assignment": "Atribuição de Política de Férias",
    "Leave Allocation": "Alocação de Férias",
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
    "Configurações": "Configurações"
};

function applyLivePortugueseTranslations() {
    // 1. App Launcher Card Title 'Suite'
    $('*').contents().filter(function() {
        if (this.nodeType !== 3) return false;
        var val = this.nodeValue.trim();
        return val === "Nacional Suite" || val === "Nacional Su..." || val.indexOf("Nacional Su") === 0;
    }).each(function() {
        var $p = $(this).parent();
        if ($p.is('.app-title, .app-name, .app-card-title, .app-caption, .desktop-icon-grid *') || 
            $p.closest('.app-card, .app-item, .desktop-icon, .grid-child').length > 0) {
            this.nodeValue = "Suite";
        }
    });

    // 2. Breadcrumbs, Titles, Number Cards, Chart Legends
    $('.breadcrumb-item, .page-title, .title-text, .widget-title, .number-card-label, .card-title, .widget-head, .legend-label, .chart-legend').each(function() {
        var $el = $(this);
        var txt = $el.text().trim();
        if (MASSIVE_PT_MAP[txt]) {
            $el.text(MASSIVE_PT_MAP[txt]);
        }
    });

    // 3. Tooltips & Sidebar
    $('.workspace-sidebar-item, .sidebar-item, .nav-item, [data-title], [title], .sidebar-item-container, .desktop-icon').each(function() {
        var $el = $(this);
        var title = $el.attr('title') || $el.attr('data-title');
        if (title && MASSIVE_PT_MAP[title.trim()]) {
            var translated = MASSIVE_PT_MAP[title.trim()];
            $el.attr('title', translated);
            $el.attr('data-title', translated);
        }
    });
}

var observer = new MutationObserver(function() {
    applyLivePortugueseTranslations();
});

$(document).on('app_ready page_change workspace_rendered chart_rendered', function() {
    if (window.frappe) {
        if (frappe.boot) {
            frappe.boot.app_name = "Nacional Suite";
        }
    }
    applyLivePortugueseTranslations();
    setTimeout(applyLivePortugueseTranslations, 200);
    setTimeout(applyLivePortugueseTranslations, 600);
    setTimeout(applyLivePortugueseTranslations, 1500);
    if (document.body) {
        try {
            observer.observe(document.body, { childList: true, subtree: true });
        } catch(e) {}
    }
});

$(document).ready(function() {
    applyLivePortugueseTranslations();
    if (document.body) {
        try {
            observer.observe(document.body, { childList: true, subtree: true });
        } catch(e) {}
    }
});
