-- ============================================================
-- PROJETO TECHPORT
-- Criação do banco, tabelas e carga de dados fictícios
--
-- Compatibilidade: MySQL 8.0+
--
-- Volumetria:
--   usuarios:     1.000
--   tecnicos:       120
--   chamados:     5.000
--   comentarios:    500
--   historicos:   1.000
--   anexos:       2.000
--
-- Observações:
-- 1. Todos os dados são fictícios.
-- 2. A geração utiliza RAND(), com distribuição uniforme.
-- 3. Não é utilizada distribuição normal.
-- 4. As datas são distribuídas aleatoriamente pelos últimos 6 meses.
-- ============================================================

DROP DATABASE IF EXISTS techport;

CREATE DATABASE techport
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE techport;

-- ============================================================
-- TABELAS
-- ============================================================

CREATE TABLE usuarios (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    email VARCHAR(180) NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    perfil VARCHAR(30) NOT NULL DEFAULT 'cliente',
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    data_cadastro DATETIME NOT NULL,
    CONSTRAINT uq_usuarios_email UNIQUE (email),
    INDEX idx_usuarios_perfil (perfil),
    INDEX idx_usuarios_ativo (ativo),
    INDEX idx_usuarios_data_cadastro (data_cadastro)
) ENGINE=InnoDB;

CREATE TABLE tecnicos (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    email VARCHAR(180) NOT NULL,
    especialidade VARCHAR(80) NOT NULL,
    nivel VARCHAR(30) NOT NULL,
    disponivel BOOLEAN NOT NULL DEFAULT TRUE,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    data_cadastro DATETIME NOT NULL,
    CONSTRAINT uq_tecnicos_email UNIQUE (email),
    INDEX idx_tecnicos_especialidade (especialidade),
    INDEX idx_tecnicos_disponivel (disponivel),
    INDEX idx_tecnicos_ativo (ativo)
) ENGINE=InnoDB;

CREATE TABLE chamados (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    usuario_id BIGINT UNSIGNED NOT NULL,
    tecnico_id BIGINT UNSIGNED NULL,
    titulo VARCHAR(180) NOT NULL,
    descricao TEXT NOT NULL,
    categoria VARCHAR(60) NOT NULL,
    prioridade VARCHAR(20) NOT NULL,
    status VARCHAR(30) NOT NULL,
    canal_abertura VARCHAR(30) NOT NULL,
    data_abertura DATETIME NOT NULL,
    data_atualizacao DATETIME NOT NULL,
    data_fechamento DATETIME NULL,

    CONSTRAINT fk_chamados_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id),

    CONSTRAINT fk_chamados_tecnico
        FOREIGN KEY (tecnico_id)
        REFERENCES tecnicos(id)
        ON DELETE SET NULL,

    INDEX idx_chamados_usuario (usuario_id),
    INDEX idx_chamados_tecnico (tecnico_id),
    INDEX idx_chamados_status (status),
    INDEX idx_chamados_prioridade (prioridade),
    INDEX idx_chamados_categoria (categoria),
    INDEX idx_chamados_data_abertura (data_abertura)
) ENGINE=InnoDB;

CREATE TABLE comentarios (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    chamado_id BIGINT UNSIGNED NOT NULL,
    usuario_id BIGINT UNSIGNED NULL,
    tecnico_id BIGINT UNSIGNED NULL,
    autor_tipo VARCHAR(20) NOT NULL,
    comentario TEXT NOT NULL,
    visibilidade VARCHAR(20) NOT NULL DEFAULT 'publico',
    data_comentario DATETIME NOT NULL,

    CONSTRAINT fk_comentarios_chamado
        FOREIGN KEY (chamado_id)
        REFERENCES chamados(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_comentarios_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE SET NULL,

    CONSTRAINT fk_comentarios_tecnico
        FOREIGN KEY (tecnico_id)
        REFERENCES tecnicos(id)
        ON DELETE SET NULL,

    INDEX idx_comentarios_chamado (chamado_id),
    INDEX idx_comentarios_data (data_comentario)
) ENGINE=InnoDB;

CREATE TABLE historico_chamados (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    chamado_id BIGINT UNSIGNED NOT NULL,
    tecnico_id BIGINT UNSIGNED NULL,
    evento VARCHAR(60) NOT NULL,
    status_anterior VARCHAR(30) NULL,
    status_novo VARCHAR(30) NULL,
    prioridade_anterior VARCHAR(20) NULL,
    prioridade_nova VARCHAR(20) NULL,
    observacao VARCHAR(500) NOT NULL,
    data_evento DATETIME NOT NULL,

    CONSTRAINT fk_historico_chamado
        FOREIGN KEY (chamado_id)
        REFERENCES chamados(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_historico_tecnico
        FOREIGN KEY (tecnico_id)
        REFERENCES tecnicos(id)
        ON DELETE SET NULL,

    INDEX idx_historico_chamado (chamado_id),
    INDEX idx_historico_evento (evento),
    INDEX idx_historico_data (data_evento)
) ENGINE=InnoDB;

CREATE TABLE anexos (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    chamado_id BIGINT UNSIGNED NOT NULL,
    usuario_id BIGINT UNSIGNED NULL,
    tecnico_id BIGINT UNSIGNED NULL,
    nome_arquivo VARCHAR(220) NOT NULL,
    tipo_mime VARCHAR(100) NOT NULL,
    tamanho_bytes BIGINT UNSIGNED NOT NULL,
    caminho_arquivo VARCHAR(500) NOT NULL,
    data_upload DATETIME NOT NULL,

    CONSTRAINT fk_anexos_chamado
        FOREIGN KEY (chamado_id)
        REFERENCES chamados(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_anexos_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE SET NULL,

    CONSTRAINT fk_anexos_tecnico
        FOREIGN KEY (tecnico_id)
        REFERENCES tecnicos(id)
        ON DELETE SET NULL,

    INDEX idx_anexos_chamado (chamado_id),
    INDEX idx_anexos_data_upload (data_upload)
) ENGINE=InnoDB;

-- ============================================================
-- PROCEDURE DE CARGA
-- ============================================================

DELIMITER $$

DROP PROCEDURE IF EXISTS popular_techport $$

CREATE PROCEDURE popular_techport()
BEGIN
    DECLARE i INT DEFAULT 1;

    DECLARE v_usuario_id BIGINT UNSIGNED;
    DECLARE v_tecnico_id BIGINT UNSIGNED;
    DECLARE v_chamado_id BIGINT UNSIGNED;

    DECLARE v_data_abertura DATETIME;
    DECLARE v_data_evento DATETIME;
    DECLARE v_data_limite DATETIME;
    DECLARE v_status VARCHAR(30);
    DECLARE v_prioridade VARCHAR(20);
    DECLARE v_autor_tipo VARCHAR(20);
    DECLARE v_extensao VARCHAR(10);
    DECLARE v_mime VARCHAR(100);

    -- --------------------------------------------------------
    -- 1. USUÁRIOS: 1.000
    -- --------------------------------------------------------
    SET i = 1;

    WHILE i <= 1000 DO
        INSERT INTO usuarios (
            nome,
            email,
            senha_hash,
            perfil,
            ativo,
            data_cadastro
        )
        VALUES (
            CONCAT(
                ELT(
                    1 + FLOOR(RAND() * 20),
                    'Alex', 'Bruno', 'Camila', 'Daniel', 'Eduarda',
                    'Felipe', 'Gabriela', 'Henrique', 'Isabela', 'João',
                    'Karen', 'Lucas', 'Marina', 'Nicolas', 'Olívia',
                    'Paulo', 'Renata', 'Samuel', 'Talita', 'Vinícius'
                ),
                ' ',
                ELT(
                    1 + FLOOR(RAND() * 20),
                    'Almeida', 'Barbosa', 'Cardoso', 'Dias', 'Esteves',
                    'Ferreira', 'Gomes', 'Lima', 'Machado', 'Nunes',
                    'Oliveira', 'Pereira', 'Queiroz', 'Ramos', 'Silva',
                    'Teixeira', 'Vieira', 'Xavier', 'Moraes', 'Costa'
                ),
                ' ',
                LPAD(i, 4, '0')
            ),
            CONCAT('usuario', LPAD(i, 4, '0'), '@techport-ficticio.local'),
            CONCAT('$2b$12$ficticio_', SHA2(CONCAT('usuario-', i), 256)),
            ELT(1 + FLOOR(RAND() * 3), 'cliente', 'gestor', 'administrador'),
            IF(RAND() < 0.92, TRUE, FALSE),
            TIMESTAMPADD(
                SECOND,
                FLOOR(RAND() * (183 * 24 * 60 * 60)),
                DATE_SUB(NOW(), INTERVAL 6 MONTH)
            )
        );

        SET i = i + 1;
    END WHILE;

    -- --------------------------------------------------------
    -- 2. TÉCNICOS: 120
    -- --------------------------------------------------------
    SET i = 1;

    WHILE i <= 120 DO
        INSERT INTO tecnicos (
            nome,
            email,
            especialidade,
            nivel,
            disponivel,
            ativo,
            data_cadastro
        )
        VALUES (
            CONCAT(
                ELT(
                    1 + FLOOR(RAND() * 15),
                    'André', 'Beatriz', 'Carlos', 'Débora', 'Emerson',
                    'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Juliana',
                    'Leandro', 'Mônica', 'Rafael', 'Sabrina', 'Tiago'
                ),
                ' ',
                ELT(
                    1 + FLOOR(RAND() * 15),
                    'Azevedo', 'Batista', 'Campos', 'Duarte', 'Farias',
                    'Garcia', 'Lopes', 'Martins', 'Mendes', 'Pinto',
                    'Rocha', 'Santos', 'Souza', 'Torres', 'Valente'
                ),
                ' ',
                LPAD(i, 3, '0')
            ),
            CONCAT('tecnico', LPAD(i, 3, '0'), '@techport-ficticio.local'),
            ELT(
                1 + FLOOR(RAND() * 8),
                'Redes',
                'Infraestrutura',
                'Sistemas',
                'Banco de Dados',
                'Segurança',
                'Suporte ao Usuário',
                'Aplicações Web',
                'Cloud'
            ),
            ELT(1 + FLOOR(RAND() * 3), 'júnior', 'pleno', 'sênior'),
            IF(RAND() < 0.70, TRUE, FALSE),
            IF(RAND() < 0.95, TRUE, FALSE),
            TIMESTAMPADD(
                SECOND,
                FLOOR(RAND() * (183 * 24 * 60 * 60)),
                DATE_SUB(NOW(), INTERVAL 6 MONTH)
            )
        );

        SET i = i + 1;
    END WHILE;

    -- --------------------------------------------------------
    -- 3. CHAMADOS: 5.000
    -- Datas distribuídas aleatoriamente nos últimos 6 meses.
    -- --------------------------------------------------------
    SET i = 1;

    WHILE i <= 5000 DO
        SET v_usuario_id = 1 + FLOOR(RAND() * 1000);
        SET v_tecnico_id = 1 + FLOOR(RAND() * 120);

        SET v_data_abertura = TIMESTAMPADD(
            SECOND,
            FLOOR(RAND() * (183 * 24 * 60 * 60)),
            DATE_SUB(NOW(), INTERVAL 6 MONTH)
        );

        SET v_status = ELT(
            1 + FLOOR(RAND() * 6),
            'aberto',
            'em_triagem',
            'em_atendimento',
            'aguardando_cliente',
            'resolvido',
            'fechado'
        );

        SET v_prioridade = ELT(
            1 + FLOOR(RAND() * 4),
            'baixa',
            'media',
            'alta',
            'critica'
        );

        INSERT INTO chamados (
            usuario_id,
            tecnico_id,
            titulo,
            descricao,
            categoria,
            prioridade,
            status,
            canal_abertura,
            data_abertura,
            data_atualizacao,
            data_fechamento
        )
        VALUES (
            v_usuario_id,
            IF(RAND() < 0.12, NULL, v_tecnico_id),
            CONCAT(
                ELT(
                    1 + FLOOR(RAND() * 12),
                    'Falha de acesso',
                    'Sistema indisponível',
                    'Erro na autenticação',
                    'Solicitação de permissão',
                    'Lentidão na aplicação',
                    'Problema no equipamento',
                    'Falha de rede',
                    'Erro no relatório',
                    'Dúvida de utilização',
                    'Solicitação de instalação',
                    'Falha no banco de dados',
                    'Problema no e-mail'
                ),
                ' #',
                LPAD(i, 5, '0')
            ),
            CONCAT(
                'Registro fictício gerado para testes. Cenário ',
                LPAD(i, 5, '0'),
                ': ',
                ELT(
                    1 + FLOOR(RAND() * 10),
                    'o usuário informou comportamento intermitente.',
                    'a falha ocorreu sem uma sequência identificável.',
                    'o problema foi percebido durante uma operação cotidiana.',
                    'não foi possível reproduzir o erro inicialmente.',
                    'há necessidade de análise técnica.',
                    'o impacto informado varia conforme o ambiente.',
                    'a ocorrência não possui padrão definido.',
                    'foram fornecidas evidências parciais.',
                    'o atendimento exige validação adicional.',
                    'a solicitação foi registrada para investigação.'
                )
            ),
            ELT(
                1 + FLOOR(RAND() * 10),
                'Hardware',
                'Software',
                'Rede',
                'Acesso',
                'E-mail',
                'Banco de Dados',
                'Segurança',
                'Impressão',
                'Aplicação Web',
                'Infraestrutura'
            ),
            v_prioridade,
            v_status,
            ELT(
                1 + FLOOR(RAND() * 5),
                'portal',
                'email',
                'telefone',
                'chat',
                'whatsapp'
            ),
            v_data_abertura,
            TIMESTAMPADD(
                SECOND,
                FLOOR(
                    RAND() * GREATEST(
                        TIMESTAMPDIFF(SECOND, v_data_abertura, NOW()),
                        1
                    )
                ),
                v_data_abertura
            ),
            CASE
                WHEN v_status IN ('resolvido', 'fechado') THEN
                    TIMESTAMPADD(
                        SECOND,
                        FLOOR(
                            RAND() * GREATEST(
                                TIMESTAMPDIFF(SECOND, v_data_abertura, NOW()),
                                1
                            )
                        ),
                        v_data_abertura
                    )
                ELSE NULL
            END
        );

        SET i = i + 1;
    END WHILE;

    -- --------------------------------------------------------
    -- 4. COMENTÁRIOS: 500
    -- Cada comentário é vinculado a um chamado aleatório.
    -- --------------------------------------------------------
    SET i = 1;

    WHILE i <= 500 DO
        SET v_chamado_id = 1 + FLOOR(RAND() * 5000);
        SET v_usuario_id = 1 + FLOOR(RAND() * 1000);
        SET v_tecnico_id = 1 + FLOOR(RAND() * 120);
        SET v_autor_tipo = IF(RAND() < 0.50, 'usuario', 'tecnico');

        SELECT data_abertura
          INTO v_data_abertura
          FROM chamados
         WHERE id = v_chamado_id;

        SET v_data_evento = TIMESTAMPADD(
            SECOND,
            FLOOR(
                RAND() * GREATEST(
                    TIMESTAMPDIFF(SECOND, v_data_abertura, NOW()),
                    1
                )
            ),
            v_data_abertura
        );

        INSERT INTO comentarios (
            chamado_id,
            usuario_id,
            tecnico_id,
            autor_tipo,
            comentario,
            visibilidade,
            data_comentario
        )
        VALUES (
            v_chamado_id,
            IF(v_autor_tipo = 'usuario', v_usuario_id, NULL),
            IF(v_autor_tipo = 'tecnico', v_tecnico_id, NULL),
            v_autor_tipo,
            ELT(
                1 + FLOOR(RAND() * 10),
                'Informação adicional registrada para análise.',
                'O comportamento voltou a ocorrer em outro horário.',
                'Foi realizado um teste sem resultado conclusivo.',
                'O atendimento permanece em investigação.',
                'Foi solicitada uma nova evidência ao usuário.',
                'A configuração foi revisada parcialmente.',
                'O cenário foi encaminhado para outra equipe.',
                'O problema não apresentou repetição durante o teste.',
                'Uma alternativa temporária foi orientada.',
                'O chamado recebeu nova atualização técnica.'
            ),
            IF(RAND() < 0.80, 'publico', 'interno'),
            v_data_evento
        );

        SET i = i + 1;
    END WHILE;

    -- --------------------------------------------------------
    -- 5. HISTÓRICO: 1.000
    --
    -- As datas são geradas de forma randômica:
    -- - entre a abertura do chamado e a data atual;
    -- - dentro da janela máxima dos últimos 6 meses;
    -- - sem sequência incremental obrigatória;
    -- - sem distribuição normal.
    -- --------------------------------------------------------
    SET i = 1;

    WHILE i <= 1000 DO
        SET v_chamado_id = 1 + FLOOR(RAND() * 5000);
        SET v_tecnico_id = 1 + FLOOR(RAND() * 120);

        SELECT data_abertura
          INTO v_data_abertura
          FROM chamados
         WHERE id = v_chamado_id;

        SET v_data_limite = NOW();

        SET v_data_evento = TIMESTAMPADD(
            SECOND,
            FLOOR(
                RAND() * GREATEST(
                    TIMESTAMPDIFF(SECOND, v_data_abertura, v_data_limite),
                    1
                )
            ),
            v_data_abertura
        );

        INSERT INTO historico_chamados (
            chamado_id,
            tecnico_id,
            evento,
            status_anterior,
            status_novo,
            prioridade_anterior,
            prioridade_nova,
            observacao,
            data_evento
        )
        VALUES (
            v_chamado_id,
            IF(RAND() < 0.15, NULL, v_tecnico_id),
            ELT(
                1 + FLOOR(RAND() * 8),
                'criacao',
                'alteracao_status',
                'alteracao_prioridade',
                'atribuicao_tecnico',
                'reabertura',
                'comentario_interno',
                'encaminhamento',
                'encerramento'
            ),
            ELT(
                1 + FLOOR(RAND() * 6),
                'aberto',
                'em_triagem',
                'em_atendimento',
                'aguardando_cliente',
                'resolvido',
                'fechado'
            ),
            ELT(
                1 + FLOOR(RAND() * 6),
                'aberto',
                'em_triagem',
                'em_atendimento',
                'aguardando_cliente',
                'resolvido',
                'fechado'
            ),
            ELT(
                1 + FLOOR(RAND() * 4),
                'baixa',
                'media',
                'alta',
                'critica'
            ),
            ELT(
                1 + FLOOR(RAND() * 4),
                'baixa',
                'media',
                'alta',
                'critica'
            ),
            CONCAT(
                'Evento fictício ',
                LPAD(i, 4, '0'),
                ': ',
                ELT(
                    1 + FLOOR(RAND() * 10),
                    'alteração registrada automaticamente.',
                    'atualização realizada após análise.',
                    'mudança efetuada sem padrão temporal.',
                    'registro incluído para rastreabilidade.',
                    'ação executada durante o atendimento.',
                    'evento gerado para teste de auditoria.',
                    'movimentação realizada por fluxo interno.',
                    'atualização vinculada ao ciclo do chamado.',
                    'registro técnico incluído no histórico.',
                    'mudança fictícia para validação do sistema.'
                )
            ),
            v_data_evento
        );

        SET i = i + 1;
    END WHILE;

    -- --------------------------------------------------------
    -- 6. ANEXOS: 2.000
    -- Somente metadados fictícios; nenhum arquivo real é criado.
    -- --------------------------------------------------------
    SET i = 1;

    WHILE i <= 2000 DO
        SET v_chamado_id = 1 + FLOOR(RAND() * 5000);
        SET v_usuario_id = 1 + FLOOR(RAND() * 1000);
        SET v_tecnico_id = 1 + FLOOR(RAND() * 120);

        SELECT data_abertura
          INTO v_data_abertura
          FROM chamados
         WHERE id = v_chamado_id;

        SET v_data_evento = TIMESTAMPADD(
            SECOND,
            FLOOR(
                RAND() * GREATEST(
                    TIMESTAMPDIFF(SECOND, v_data_abertura, NOW()),
                    1
                )
            ),
            v_data_abertura
        );

        SET v_extensao = ELT(
            1 + FLOOR(RAND() * 6),
            'pdf',
            'png',
            'jpg',
            'txt',
            'log',
            'csv'
        );

        SET v_mime = CASE v_extensao
            WHEN 'pdf' THEN 'application/pdf'
            WHEN 'png' THEN 'image/png'
            WHEN 'jpg' THEN 'image/jpeg'
            WHEN 'txt' THEN 'text/plain'
            WHEN 'log' THEN 'text/plain'
            WHEN 'csv' THEN 'text/csv'
            ELSE 'application/octet-stream'
        END;

        INSERT INTO anexos (
            chamado_id,
            usuario_id,
            tecnico_id,
            nome_arquivo,
            tipo_mime,
            tamanho_bytes,
            caminho_arquivo,
            data_upload
        )
        VALUES (
            v_chamado_id,
            IF(RAND() < 0.55, v_usuario_id, NULL),
            IF(RAND() < 0.45, v_tecnico_id, NULL),
            CONCAT(
                'anexo_ficticio_',
                LPAD(i, 5, '0'),
                '.',
                v_extensao
            ),
            v_mime,
            1024 + FLOOR(RAND() * 15728640),
            CONCAT(
                '/dados-ficticios/chamados/',
                v_chamado_id,
                '/anexo_',
                LPAD(i, 5, '0'),
                '.',
                v_extensao
            ),
            v_data_evento
        );

        SET i = i + 1;
    END WHILE;
END $$

DELIMITER ;

-- Executa a carga completa.
CALL popular_techport();

-- Remove a procedure após a utilização.
DROP PROCEDURE IF EXISTS popular_techport;

-- ============================================================
-- VALIDAÇÃO DA VOLUMETRIA
-- ============================================================

SELECT 'usuarios' AS tabela, COUNT(*) AS total FROM usuarios
UNION ALL
SELECT 'tecnicos', COUNT(*) FROM tecnicos
UNION ALL
SELECT 'chamados', COUNT(*) FROM chamados
UNION ALL
SELECT 'comentarios', COUNT(*) FROM comentarios
UNION ALL
SELECT 'historico_chamados', COUNT(*) FROM historico_chamados
UNION ALL
SELECT 'anexos', COUNT(*) FROM anexos;

-- ============================================================
-- VALIDAÇÃO DO INTERVALO DAS DATAS
-- ============================================================

SELECT
    MIN(data_abertura) AS primeira_abertura,
    MAX(data_abertura) AS ultima_abertura
FROM chamados;

SELECT
    MIN(data_evento) AS primeiro_evento,
    MAX(data_evento) AS ultimo_evento,
    COUNT(*) AS total_eventos
FROM historico_chamados;

-- Distribuição mensal para conferência.
-- Os valores variam a cada execução porque a geração é randômica.
SELECT
    DATE_FORMAT(data_evento, '%Y-%m') AS mes,
    COUNT(*) AS quantidade
FROM historico_chamados
GROUP BY DATE_FORMAT(data_evento, '%Y-%m')
ORDER BY mes;
