# Status Nacional Suite

Atualizado em 2026-08-11.

## Produção atual

- Domínio: https://suite.nacionalcarness.com.br
- VPS/IP: 74.1.21.111
- Nginx: `/etc/nginx/sites-available/suite.nacionalcarnes.com.br` apontando para `127.0.0.1:8000`
- SSL: Let's Encrypt para `suite.nacionalcarness.com.br`
- Frappe container: `docker-frappe-1`
- Site Frappe: `hrms.localhost`
- Apps instalados:
  - `frappe`
  - `erpnext`
  - `hrms`
  - `nacional_suite`

## Branding aplicado

- Nome: Nacional Suite
- Logo no banco: `/assets/nacional_suite/images/suite-logo.png`
- Logo publicada no bench ativo: `sites/assets/nacional_suite/images/suite-logo.png`

## Cuidado operacional

Evitar `bench build` nesse ambiente sem necessidade: em 2026-08-11 ele travou/pesou demais. Para branding simples, preferir:

```bash
bench --site hrms.localhost execute frappe.db.set_single_value --args '["Navbar Settings","app_logo","/assets/nacional_suite/images/suite-logo.png"]'
bench --site hrms.localhost clear-cache
```

Se adicionar assets sem build, publicar manualmente:

```bash
mkdir -p sites/assets/nacional_suite/images
cp apps/nacional_suite/nacional_suite/public/images/suite-logo.png sites/assets/nacional_suite/images/suite-logo.png
```
