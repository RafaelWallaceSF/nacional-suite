/* Nacional Suite AI Assistant Floating Chat Widget */
(function() {
    if (window.NacionalAIWidgetLoaded) return;
    window.NacionalAIWidgetLoaded = true;

    var widgetHtml = `
        <div id="nacional-ai-fab" class="nacional-ai-fab" title="Assistente Virtual Nacional Suite">
            <div class="nacional-ai-fab-icon">✨</div>
            <span class="nacional-ai-fab-text">Ajuda IA</span>
        </div>

        <div id="nacional-ai-chat" class="nacional-ai-chat-box hidden">
            <div class="nacional-ai-header">
                <div class="nacional-ai-header-title">
                    <span class="nacional-ai-avatar">🤖</span>
                    <div>
                        <strong>Assistente Nacional Suite</strong>
                        <div class="nacional-ai-status">Online • Guia de Uso</div>
                    </div>
                </div>
                <button id="nacional-ai-close" class="nacional-ai-close">&times;</button>
            </div>

            <div id="nacional-ai-messages" class="nacional-ai-messages">
                <div class="nacional-ai-msg bot">
                    Olá! Sou o Assistente Virtual do <strong>Nacional Suite</strong>.<br>Como posso ajudar você a navegar no sistema hoje?
                </div>

                <div class="nacional-ai-chips">
                    <button class="nacional-ai-chip" data-q="Como demitir um funcionário?">💡 Como demitir um funcionário?</button>
                    <button class="nacional-ai-chip" data-q="Como criar uma vaga de emprego?">💡 Como criar uma vaga?</button>
                    <button class="nacional-ai-chip" data-q="Como solicitar férias?">💡 Como solicitar férias?</button>
                    <button class="nacional-ai-chip" data-q="Como lançar reembolso?">💡 Como lançar reembolso?</button>
                </div>
            </div>

            <div class="nacional-ai-footer">
                <input type="text" id="nacional-ai-input" placeholder="Pergunte como usar o sistema..." autocomplete="off">
                <button id="nacional-ai-send">Enviar</button>
            </div>
        </div>
    `;

    function formatMarkdown(text) {
        if (!text) return "";
        return text
            .replace(/^### (.*$)/gim, '<h4 style="margin: 6px 0; font-size: 14px; font-weight:700;">$1</h4>')
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');
    }

    function appendMessage(sender, text) {
        var $box = $('#nacional-ai-messages');
        var formatted = formatMarkdown(text);
        var msgClass = sender === 'user' ? 'user' : 'bot';
        var $msg = $('<div class="nacional-ai-msg ' + msgClass + '"></div>').html(formatted);
        $box.append($msg);
        $box.scrollTop($box[0].scrollHeight);
    }

    function sendQuestion(questionText) {
        if (!questionText || !questionText.trim()) return;
        var q = questionText.trim();

        appendMessage('user', q);
        $('#nacional-ai-input').val('');

        var $typing = $('<div class="nacional-ai-msg bot typing"><em>Digitando orientações...</em></div>');
        $('#nacional-ai-messages').append($typing);

        var currentRoute = window.location.hash || window.location.pathname;

        frappe.call({
            method: 'nacional_suite.api.ask_ai',
            args: {
                question: q,
                current_route: currentRoute
            },
            callback: function(r) {
                $typing.remove();
                if (r && r.message && r.message.reply) {
                    appendMessage('bot', r.message.reply);
                } else {
                    appendMessage('bot', 'Desculpe, não consegui obter essa orientação no momento. Tente utilizar a busca rápida no topo com Ctrl + K.');
                }
            },
            error: function() {
                $typing.remove();
                appendMessage('bot', 'Desculpe, ocorreu uma falha ao conectar ao assistente. Tente novamente em instantes.');
            }
        });
    }

    function initWidget() {
        if ($('#nacional-ai-fab').length === 0) {
            $('body').append(widgetHtml);
        }

        $(document).on('click', '#nacional-ai-fab', function() {
            $('#nacional-ai-chat').toggleClass('hidden');
            $('#nacional-ai-input').focus();
        });

        $(document).on('click', '#nacional-ai-close', function() {
            $('#nacional-ai-chat').addClass('hidden');
        });

        $(document).on('click', '#nacional-ai-send', function() {
            var q = $('#nacional-ai-input').val();
            sendQuestion(q);
        });

        $(document).on('keypress', '#nacional-ai-input', function(e) {
            if (e.which === 13) {
                sendQuestion($(this).val());
            }
        });

        $(document).on('click', '.nacional-ai-chip', function() {
            var q = $(this).attr('data-q');
            sendQuestion(q);
        });
    }

    $(document).ready(function() {
        initWidget();
    });
})();
