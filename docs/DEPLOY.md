# Deploy Nacional Suite

## Conceito

Não versionar fork completo de Frappe/ERPNext/HRMS. Este projeto instala os apps upstream e adiciona o app customizado `nacional_suite` por cima.

## Instalação em bench existente

```bash
cd /home/frappe/frappe-bench
bench get-app /caminho/para/nacional-suite/apps/nacional_suite
bench --site suite.nacionalcarnes.com.br install-app nacional_suite
bench --site suite.nacionalcarnes.com.br migrate
bench --site suite.nacionalcarnes.com.br clear-cache
```

## Branding

Logo: `/assets/nacional_suite/images/suite-logo.png`
Nome: `Nacional Suite`
