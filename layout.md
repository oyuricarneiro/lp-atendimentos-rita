# Layout Spec - Consulta Nutricional Inicial | Dra. Rita Castro

## Design System (extraído do hero + problema aprovados)

### Paleta de Cores
| Token | Hex | Uso |
|-------|-----|-----|
| --forest | #103824 | Backgrounds escuros, headlines |
| --cta-green | #349D01 | CTAs, destaques, labels |
| --cta-green-hover | #2b8101 | Hover do CTA |
| --mint | #93DA9E | Acentos, ícones, itálicos |
| --mint-light | rgba(147,218,158,.12) | Backgrounds suaves de ícones |
| --off-white | #F7F7F5 | Backgrounds claros alternados |
| --white | #FFFFFF | Fundo padrão |
| --text | #191613 | Texto principal |
| --text-light | #5C5D5C | Texto secundário |
| --border | #E6E6E6 | Bordas |

### Tipografia
- **Heading:** Newsreader (400, 500, 600, 700, 800 + italic 400, 500)
- **Body:** Manrope (300, 400, 500, 600, 700)

### Tokens de Espaçamento (8pt grid)
8, 16, 24, 32, 40, 48, 64, 80, 96px

### Raios
- sm: 8px | md: 16px | lg: 24px | pill: 100px

### Sombras
- card: 0 1px 3px rgba(16,56,36,.04), 0 4px 16px rgba(16,56,36,.06)
- card-hover: 0 2px 8px rgba(16,56,36,.06), 0 8px 32px rgba(16,56,36,.10)
- photo: 0 8px 40px rgba(16,56,36,.12)

### Max-width: 1120px

### Imagens Disponíveis e Uso Decidido
| Arquivo | Conteúdo | Usar? | Onde |
|---------|----------|-------|------|
| imgi_6_Rectangle-6696_1x.webp | Dra. Rita sorrindo na natureza (verde) | SIM - já no hero | Hero |
| imgi_7_Rectangle-6700_1x.webp | Dra. Rita no laptop em ambiente natural | SIM | Seção Metodologia |
| imgi_9_Rectangle-6697_1x.webp | Dra. Rita palestrando com telas e plateia | SIM | Seção Quem É |
| imgi_8_Rectangle-6699_1x.webp | Dra. Rita conversando com participantes | SIM | Seção Depoimentos (ambiente) |
| imgi_10_Rectangle-6698_1x.webp | Dra. Rita no palco (chapéu vermelho) | NAO | Paleta de cor conflita (roxo/vermelho) |
| imgi_25_BG-DKTP-1.webp | Background com foto palestra + overlay forest | SIM | Seção Quem É (background) |
| imgi_2_Group-1171276295.webp | Ícone aspas (círculo forest) | SIM | Depoimentos |
| imgi_4_Group.webp | Ícone play video (mint) | SIM | Menção à gravação |
| imgi_1_LOGO-1.webp | Logo Comunidade da Longevidade | SIM | Seção Quem É (credencial) |
| imgi_3_3-3.webp | Logo Universidade Biohacker (branca) | SIM | Seção Quem É (credencial) |
| imgi_5_Group-1171275016-922x1024.webp | Selo de Garantia hexagonal | NAO | Não há garantia na copy |
| imgi_18_Group-1707478786-2.webp | Infográfico Luz/Sono/Alimentação/Micronutrientes | NAO | Genérico, não conversa com a copy |

---

## Seção 1: Hero (JÁ APROVADO - manter exatamente como está)

O hero já está implementado e aprovado no index.html + style.css. MANTER INALTERADO.

**Resumo do que existe:**
- Background --forest com radial gradient mint sutil
- Grid 1fr 1fr: conteúdo à esquerda, foto à direita
- Eyebrow mint uppercase, headline Newsreader 700 com `em` em mint, subheadline rgba branco
- CTA pill verde com seta animada
- Microcopy com ícone relógio
- Foto com shape offset mint + floaters glassmorphism com parallax no mouse
- Chips bar com entregáveis na base
- Responsivo: stack vertical, foto topo, floaters hidden mobile

---

## Seção 2: Problema-Oportunidade (JÁ APROVADO - manter exatamente como está)

Já implementado e aprovado. MANTER INALTERADO.

**Resumo do que existe:**
- Background gradient mint-light para branco
- Label pill verde, headline Newsreader forest, subheadline text-light
- Bloco intro com border-left mint
- Grid 2col de sinais com ícones SVG em cards com hover lift
- Grid 4col de momentos de vida com cards arredondados + ícones circulares
- Bloco oportunidade forest com accent bar cta-green
- CTA centralizado verde

---

## Seção 3: Depoimentos

### Arquétipo e Constraints
- **Arquétipo:** Editorial (layout de revista com tipografia elaborada e composição assimétrica)
- **Constraints:** Texto com Gradiente + Overlap Elements + Stagger Animation
- **Justificativa:** Depoimentos são prova social - precisam de destaque tipográfico forte e apresentação não-convencional. O arquétipo editorial evita o padrão genérico de carousel com foto circular. O overlap cria profundidade e sofisticação high-ticket.

### Conteúdo
- **Headline:** O que muda quando existe clareza
- **Depoimento 1:** "Eu já tinha tentado várias coisas. A consulta me deu direção: o que priorizar, o que parar de fazer e como organizar a rotina de um jeito possível." — Karina, 42
- **Depoimento 2:** "Não foi 'mais um protocolo'. Foi entender meu corpo e sair com plano alimentar, prescrição e exames certos pra investigar." — Ângela, 53
- **Depoimento 3:** "Eu vivia cansada e sem constância. A clareza das prioridades e os ajustes práticos foram o que destravaram." — Rafaela, 35
- **CTA:** QUERO ME CANDIDATAR À CONSULTA INICIAL

### Layout

**Desktop (>960px):**
- Background: --off-white (#F7F7F5) com noise texture sutil (CSS grain via pseudo-element, opacity 0.03)
- Padding: 96px 0
- Container: max-width 1120px centralizado, padding 0 32px

**Headline:**
- Posição: alinhada à esquerda
- Largura: max-width 500px
- Margin-bottom: 64px

**Depoimentos - Layout Staggered Vertical:**
- NÃO é carousel. É layout vertical com cards escalonados.
- 3 cards dispostos em coluna única, max-width 780px, centralizado
- Cada card tem margin-left alternado para criar efeito zigzag:
  - Card 1: margin-left: 0
  - Card 2: margin-left: 120px
  - Card 3: margin-left: 40px

**Estrutura de cada Card:**
- Background: --white
- Border: 1px solid --border
- Border-radius: 24px
- Padding: 40px 48px
- Position: relative
- Margin-bottom: 32px (entre cards)
- Transition: border-color .3s ease, box-shadow .3s ease, transform .3s ease

**Dentro de cada card:**
- Ícone de aspas SVG: usar imgi_2_Group-1171276295.webp (48x48px, opacity 0.15, position absolute, top 24px, right 32px)
- Texto do depoimento: Newsreader italic 400, 20px desktop / 17px mobile, line-height 1.7, color --text, margin-bottom 20px
- Linha separadora: width 40px, height 2px, background --mint, margin-bottom 16px
- Nome: Manrope 600, 14px, uppercase, letter-spacing 0.06em, color --forest
- EM SEGUIDA à virgula, idade em Manrope 400, 14px, color --text-light

**Elemento decorativo lateral:**
- Linha vertical tracejada em --mint (opacity 0.2), position absolute, left -60px, top 0, height 100% do container de depoimentos
- Pequenos círculos (8px) em --mint preenchido nos pontos onde cada card começa (posição left: -64px, centralizado na linha)
- Isso cria um efeito de "timeline" sutil conectando os depoimentos

### Tipografia
- **Headline:** Newsreader 700, clamp(28px, 3vw, 40px), line-height 1.2, letter-spacing -0.01em, color --forest
- **Headline "clareza":** envolver em `<em>` com color --cta-green, font-style normal
- **Depoimento texto:** Newsreader italic 400, clamp(16px, 1.3vw, 20px), line-height 1.7, color --text
- **Nome:** Manrope 600, 14px, letter-spacing 0.06em, text-transform uppercase, color --forest
- **Idade:** Manrope 400, 14px, color --text-light

### Cores
- Background seção: --off-white (#F7F7F5)
- Cards: --white (#FFFFFF)
- Borda cards normal: --border (#E6E6E6)
- Borda cards hover: --mint (#93DA9E)
- Sombra cards hover: --shadow-card-hover
- Aspas icon: opacity 0.12
- Linha separadora: --mint (#93DA9E)
- Timeline lateral: --mint com opacity 0.2
- Dots timeline: --mint solid

### Elementos Visuais
- Ícone de aspas: imgi_2_Group-1171276295.webp, 48x48, opacity 0.12, decorativo
- Noise texture no background: pseudo-element ::after com background: url(data:image/svg+xml... noise), opacity 0.03
- Timeline lateral com dots (CSS puro, usando ::before nos cards + border-left dashed no container)

### Animações
- **Cards:** data-aos="fade-up", cada card com delay incremental
  - Card 1: delay 0ms
  - Card 2: delay 150ms
  - Card 3: delay 300ms
  - Duration: 800ms, ease-out
- **Hover cards:** translateY(-4px) + box-shadow transition para --shadow-card-hover, 300ms ease
- **Linha separadora dentro do card:** no hover, width anima de 40px para 80px, 400ms cubic-bezier(0.16, 1, 0.3, 1)

### Interatividade
- **Hover no card:** border-color muda para --mint, sombra para --shadow-card-hover, translateY(-4px)
- **Hover na linha separadora:** expande de 40px para 80px com transição suave

### Responsividade
**Tablet (<=960px):**
- Cards: margin-left 0 em todos (sem zigzag)
- Timeline lateral: hidden
- Padding cards: 32px 36px

**Mobile (<=600px):**
- Padding seção: 64px 0
- Cards padding: 24px 28px
- Texto depoimento: 16px
- Headline: 26px
- Margin-bottom entre cards: 24px

---

## Seção 4: Metodologia (Como Funciona)

### Arquétipo e Constraints
- **Arquétipo:** Scroll Storytelling (narrativa que se desenrola com scroll, etapas reveladas progressivamente)
- **Constraints:** Split Assimétrico (60/40) + Sticky Element + Stagger Animation + Numbered Steps
- **Justificativa:** Mostrar um processo de 4 etapas precisa de narrativa sequencial e visual. O split assimétrico com foto sticky de um lado e etapas rolando do outro cria uma experiência imersiva e editorial, evitando o clichê de timeline simples.

### Conteúdo
- **Headline:** Entregáveis fixos. Plano personalizado. Execução possível.
- **Subheadline:** O método parte de um princípio: os entregáveis são fixos, e o plano é personalizado conforme necessidades, exames e prioridades.

**Etapa 1: Candidatura**
Você preenche seus dados e responde: "Qual é seu maior desafio de saúde atual?"

**Etapa 2: Organização pré-consulta**
Você envia exames e informações relevantes (quando tiver), para aumentar a precisão da avaliação.

**Etapa 3: Consulta Nutricional Inicial - 2h com a Dra. Rita**
Consulta online, completa e estratégica.

**Etapa 4: Entregáveis da consulta (o que você leva)**
- Revisão dos exames enviados
- interpretação de teste genéticos e exames (quando necessário, para investigar o que realmente importa no seu caso)
- Prescrição (conforme avaliação e prioridade)
- Plano alimentar aplicado à sua rotina
- Plano inicial de 30-90 dias (com prioridades e sequência)
Formato: online, com gravação no app.

**Sub-bloco: O que a consulta pode contemplar:**
- Longevidade e consistência (energia, composição corporal, performance e rotina)
- Perimenopausa/menopausa (sintomas, sono, humor e metabolismo)
- Fertilidade / preparo para engravidar (estratégia e execução com clareza)
- Intestino, inflamação e sintomas recorrentes (quando esse é o eixo do seu caso)
- Sono, ansiedade e foco (quando isso está travando o resto)

- **CTA:** QUERO ME CANDIDATAR À CONSULTA INICIAL

### Layout

**Desktop (>960px):**
- Background: --white
- Padding: 96px 0
- Container: max-width 1120px

**Header:**
- Label pill: "Como funciona" — mesmo estilo do problema__label (12px, 600, uppercase, letter-spacing 0.1em, background rgba(52,157,1,.08), color --cta-green, padding 6px 16px, border-radius pill)
- Headline: max-width 700px, margin-bottom 24px
- Subheadline: max-width 600px, margin-bottom 64px
- Alinhamento: esquerda

**Layout do processo - Split 60/40:**
- display: grid, grid-template-columns: 1fr 420px, gap 64px, align-items start
- Coluna esquerda (60%): Etapas empilhadas verticalmente
- Coluna direita (40%): Imagem sticky

**Coluna direita - Imagem sticky:**
- position: sticky, top: 120px
- Imagem: imgi_7_Rectangle-6700_1x.webp (Dra. Rita no laptop)
- border-radius: 24px
- box-shadow: --shadow-photo
- Aspect-ratio: 3/2
- Decorativo: borda sutil de 3px --mint-light ao redor (com gap de 8px usando outline + outline-offset)

**Coluna esquerda - Cards de etapas:**
Cada etapa é um bloco:
- Margin-bottom: 48px (entre etapas)
- Display: flex, gap 24px

**Número da etapa (lado esquerdo do card):**
- Width: 48px, height: 48px, min-width: 48px
- Background: --forest
- Color: --white
- Border-radius: 50%
- Display: flex, align-items center, justify-content center
- Font: Newsreader 700, 20px
- Flex-shrink: 0

**Conteúdo da etapa (lado direito):**
- **Título:** Manrope 600, 18px, color --forest, margin-bottom 8px, line-height 1.4
- **Descrição:** Manrope 400, 15px, line-height 1.7, color --text-light
- **Lista (etapa 4):** styled com checkmarks SVG em --cta-green, 14px, line-height 1.8, margin-top 12px

**Entre etapas 1-3:** Linha vertical pontilhada conectando os números (border-left: 2px dashed rgba(147,218,158,0.3), position absolute, left 23px (centro do número), top 48px, height calc(100% - 48px))

**Etapa 4 - Destaque especial:**
- Background: --off-white
- Border-radius: 20px
- Padding: 32px
- Border-left: 3px solid --cta-green
- O número 4 tem background --cta-green em vez de --forest

**Sub-bloco "O que a consulta pode contemplar":**
- Separado por margin-top 48px e border-top 1px solid --border
- Padding-top: 48px
- Título: Newsreader 600, 20px, color --forest, margin-bottom 24px
- Itens em lista com bullets customizados:
  - Bullet: círculo 6px, background --mint, margin-right 12px
  - Texto: Manrope 400, 15px, line-height 1.7, color --text
  - Cada item tem margin-bottom 16px
  - Dentro de cada item, o texto entre parênteses tem color --text-light

### Tipografia
- **Label:** Manrope 600, 12px, letter-spacing 0.1em, uppercase, --cta-green
- **Headline:** Newsreader 700, clamp(28px, 3.2vw, 42px), line-height 1.2, letter-spacing -0.01em, color --forest
- **Subheadline:** Manrope 400, clamp(15px, 1.1vw, 17px), line-height 1.7, color --text-light
- **Número etapa:** Newsreader 700, 20px, --white
- **Título etapa:** Manrope 600, 18px, color --forest
- **Descrição etapa:** Manrope 400, 15px, line-height 1.7, --text-light
- **Itens lista entregáveis:** Manrope 400, 14px, line-height 1.8, --text
- **Título sub-bloco:** Newsreader 600, 20px, --forest

### Cores
- Background seção: --white
- Números 1-3: bg --forest, texto --white
- Número 4: bg --cta-green, texto --white
- Etapa 4 card: bg --off-white, border-left --cta-green
- Checkmarks lista: --cta-green
- Linha conectora: --mint opacity 0.3
- Bullets sub-bloco: --mint

### Elementos Visuais
- Imagem imgi_7_Rectangle-6700_1x.webp com border-radius 24px e shadow
- Outline decorativo mint-light na imagem
- Linha pontilhada vertical conectando números das etapas (CSS)
- Checkmarks SVG inline para lista de entregáveis
- Ícone play (imgi_4_Group.webp, 20x20, inline) ao lado de "online, com gravação no app"

### Animações
- **Header:** fade-up 800ms ease-out
- **Etapas:** cada card com data-aos="fade-up", delay stagger:
  - Etapa 1: delay 0
  - Etapa 2: delay 100ms
  - Etapa 3: delay 200ms
  - Etapa 4: delay 300ms
- **Números:** counter animation sutil - número aparece com scale(0) para scale(1), 400ms cubic-bezier(0.34, 1.56, 0.64, 1) (efeito spring), triggered junto com o fade-up do card
- **Imagem sticky:** fade-in inicial ao entrar no viewport, 600ms ease

### Interatividade
- **Hover nas etapas (não na 4):** translateY(-2px), border-left 3px solid --mint aparece da esquerda (width 0 para 3px), 300ms ease
- **Hover na etapa 4:** box-shadow --shadow-card, 300ms ease
- **Imagem sticky:** leve parallax no scroll (translateY com scroll speed 0.05 - CSS scroll-driven se suportado, senão sem parallax)

### Responsividade
**Tablet (<=960px):**
- Grid: 1fr (coluna única)
- Imagem: não sticky, aparece antes das etapas, max-width 560px, margin 0 auto 48px
- Etapas: sem mudança

**Mobile (<=600px):**
- Padding seção: 64px 0
- Headline: 26px
- Etapas: gap 16px, margin-bottom 32px
- Número: 40x40, font 17px
- Linha conectora: left 19px
- Etapa 4 padding: 24px
- Sub-bloco: margin-top 32px

---

## Seção 5: O Que Você Vai Ter Clareza

### Arquétipo e Constraints
- **Arquétipo:** Bento Box (células de tamanhos variados como caixa bento japonesa)
- **Constraints:** Glassmorphism + Hover Reveal + Scale In Animation
- **Justificativa:** Os 6 bullet points da copy são entregáveis concretos. O Bento Box evita a lista genérica e cria uma composição visual rica (variação de tamanhos = hierarquia visual). Glassmorphism nos cards reforça o tom premium/high-ticket. Hover reveal adiciona camada de interatividade.

### Conteúdo
- **Headline:** Você sai com um plano — não com uma lista de possibilidades
- **Items:**
  1. O que é prioridade no seu caso (e o que é só barulho)
  2. Quais exames fazem sentido pedir agora (e por quê)
  3. Plano alimentar que conversa com sua rotina (e não com uma "vida ideal")
  4. Prescrição alinhada a objetivos e tolerâncias
  5. Plano inicial de 30–90 dias com sequência e foco
  6. Próximos ajustes práticos para melhorar energia, sono e sintomas com consistência
- **CTA:** QUERO ME CANDIDATAR À CONSULTA INICIAL

### Layout

**Desktop (>960px):**
- Background: --forest (#103824)
- Padding: 96px 0
- Container: max-width 1120px
- Position: relative
- Overflow: hidden

**Background decorativo:**
- Pseudo-element ::before: radial-gradient(circle at 20% 80%, rgba(147,218,158,0.06) 0%, transparent 60%), 600x600px
- Pseudo-element ::after: radial-gradient(circle at 80% 20%, rgba(52,157,1,0.04) 0%, transparent 50%), 500x500px

**Headline:**
- Color: --white
- Max-width: 600px
- Margin-bottom: 64px
- Alinhamento: esquerda

**Bento Grid:**
- display: grid
- grid-template-columns: repeat(3, 1fr)
- grid-template-rows: auto auto
- gap: 20px
- Layout das 6 células (todas ocupam 1 célula do grid, EXCETO item 3 que ocupa 2 colunas):
  - Item 1: col 1, row 1
  - Item 2: col 2, row 1
  - Item 3: col 3, row 1 / row 2 (span 2 rows) — o item mais longo, destaque vertical
  - Item 4: col 1, row 2
  - Item 5: col 2, row 2
  - Item 6: col 1-3, row 3 (span 3 colunas) — item final, barra horizontal full-width

**Cada célula Bento:**
- Background: rgba(255,255,255,0.06)
- Backdrop-filter: blur(16px)
- -webkit-backdrop-filter: blur(16px)
- Border: 1px solid rgba(255,255,255,0.1)
- Border-radius: 20px
- Padding: 32px
- Position: relative
- Overflow: hidden
- Transition: background .3s ease, border-color .3s ease, transform .3s ease

**Dentro de cada célula:**
- Ícone SVG no topo: 32x32px, color --mint, margin-bottom 20px
  - Item 1 (prioridade): ícone target/alvo
  - Item 2 (exames): ícone clipboard com check
  - Item 3 (plano alimentar): ícone folha/planta
  - Item 4 (prescrição): ícone shield com check
  - Item 5 (plano 30-90 dias): ícone calendário/roadmap
  - Item 6 (ajustes práticos): ícone settings/engrenagem com seta
- Texto: o bullet da copy, sem alterações
- Texto entre parênteses: destaque sutil em rgba(255,255,255,0.5)

**Item 3 (vertical span) tratamento especial:**
- Padding: 40px
- Display: flex, flex-direction: column, justify-content: center
- Ícone maior: 40x40px
- Borda esquerda: 3px solid --cta-green (accent)

**Item 6 (horizontal span) tratamento especial:**
- Display: flex, align-items: center, gap: 24px
- Ícone à esquerda (não acima)
- Texto em linha
- Background ligeiramente diferente: rgba(52,157,1,0.08)
- Border: 1px solid rgba(52,157,1,0.15)

### Tipografia
- **Headline:** Newsreader 700, clamp(28px, 3vw, 40px), line-height 1.2, letter-spacing -0.01em, color --white
- **Headline "plano":** envolver em `<em>` com color --mint, font-style italic
- **Texto dos itens:** Manrope 400, 16px, line-height 1.65, color rgba(255,255,255,0.82)
- **Texto parênteses:** color rgba(255,255,255,0.5)

### Cores
- Background seção: --forest (#103824)
- Cards: rgba(255,255,255,0.06) com blur
- Borda cards: rgba(255,255,255,0.1)
- Borda cards hover: rgba(255,255,255,0.2)
- Ícones: --mint (#93DA9E)
- Texto: rgba(255,255,255,0.82)
- Item 3 accent: --cta-green
- Item 6 bg: rgba(52,157,1,0.08)

### Animações
- **Cards:** data-aos="fade-up" com stagger
  - Items 1,2: delay 0
  - Item 3: delay 100ms
  - Items 4,5: delay 200ms
  - Item 6: delay 300ms
  - Duration: 700ms, ease-out
- **Ícones dentros dos cards:** quando card entra no viewport, ícone faz scale(0.5) → scale(1), 500ms cubic-bezier(0.34, 1.56, 0.64, 1), delay 200ms após o card
- **Background gradient:** animation sutil de breathing (opacity 0.04 → 0.08 → 0.04), 8s ease-in-out infinite

### Interatividade
- **Hover no card:** background muda para rgba(255,255,255,0.1), border-color para rgba(255,255,255,0.2), translateY(-3px), 300ms ease
- **Hover no ícone do card:** scale(1.15), 300ms cubic-bezier(0.16, 1, 0.3, 1)

### Responsividade
**Tablet (<=960px):**
- Grid: repeat(2, 1fr)
- Item 3: span 1 (sem vertical span)
- Item 6: span 2 (horizontal full ainda)
- Gap: 16px

**Mobile (<=600px):**
- Grid: 1fr (coluna única)
- Todos os items: span 1
- Item 6: span 1, flex-direction column (ícone acima)
- Padding seção: 64px 0
- Cards padding: 24px
- Headline: 26px

---

## Seção 6: Quem É a Dra. Rita Castro

### Arquétipo e Constraints
- **Arquétipo:** Split Vertical com Overlap (divisão 50/50 onde conteúdos se cruzam na fronteira)
- **Constraints:** Imagem com Overlay + Texto com Gradiente + Floating Cards + Mouse Parallax
- **Justificativa:** Bio da profissional precisa de impacto visual e autoridade. O split cria uma composição premium, com a foto em uma metade e texto na outra. O overlap de logos/credenciais na fronteira conecta visualmente imagem e texto. O gradiente no nome reforça branding.

### Conteúdo
- **Headline:** Ciência aplicada com estratégia clínica — sem modismos, sem achismos
- **Bio parágrafo 1:** Dra. Rita Castro é nutricionista, Mestre em Ciências pela USP, com especializações nos EUA em Nutrigenômica, Nutrigenética e Epigenética. Pioneira no Brasil em biohacking e epigenética aplicada à saúde, longevidade e performance, atua há mais de 15 anos integrando ciência, estratégia e abordagem integrativa.
- **Bio parágrafo 2:** É fundadora da Universidade do Biohacker, onde forma profissionais de saúde capazes de transformar complexidade em conduta clínica segura, ética e personalizada, além de criadora da Comunidade da Longevidade e da Casa Biohacker.
- **Bio parágrafo 3:** Autora de quatro livros, sua missão é ensinar pessoas e profissionais a compreenderem o corpo como um laboratório de reprogramação epigenética unindo ciência, natureza e consciência para uma vida com mais vitalidade e propósito.
- **CTA:** QUERO ME CANDIDATAR À CONSULTA INICIAL

### Layout

**Desktop (>960px):**
- Background: --off-white (#F7F7F5)
- Padding: 96px 0
- Container: max-width 1120px

**Grid principal:**
- display: grid
- grid-template-columns: 1fr 1fr
- gap: 0 (sem gap, as colunas se conectam)
- align-items: center

**Coluna esquerda - Visual:**
- Position: relative
- Padding-right: 40px

**Imagem principal:**
- Imagem: imgi_9_Rectangle-6697_1x.webp (Dra. Rita palestrando)
- Width: 100%
- Border-radius: 24px 0 0 24px (arredondado apenas lado esquerdo)
- Box-shadow: --shadow-photo
- Aspect-ratio: 3/2
- Object-fit: cover

**Background decorativo atrás da imagem:**
- Usar imgi_25_BG-DKTP-1.webp como background-image com opacity 0.15 via pseudo-element
- Position absolute, inset -20px, z-index -1
- Border-radius: 32px
- Filter: blur(20px)

**Cards de credenciais flutuantes (sobre a imagem, overlap para a direita):**
- Position: absolute
- Z-index: 3

Card credencial 1 (bottom-left):
- Bottom: 40px, left: 20px
- Background: rgba(255,255,255,0.92)
- Backdrop-filter: blur(12px)
- Border: 1px solid rgba(255,255,255,0.6)
- Border-radius: 16px
- Padding: 12px 20px
- Display: flex, align-items: center, gap: 12px
- Conteúdo: "Mestre em Ciências — USP" + mini ícone graduation cap SVG (20x20, --forest)
- Font: Manrope 500, 13px, --forest

Card credencial 2 (top-right, overlap na fronteira):
- Top: 32px, right: -60px (ultrapassa a coluna para a direita)
- Mesmo estilo que card 1
- Conteúdo: "+15 anos de atuação" + ícone estrela SVG
- Font: Manrope 600, 13px, --forest

Card credencial 3 (bottom-right, overlap na fronteira):
- Bottom: 80px, right: -40px
- Mesmo estilo mas menor
- Conteúdo: "4 livros publicados" + ícone book SVG

**Coluna direita - Texto:**
- Padding-left: 60px

**Headline:**
- Margin-bottom: 32px

**Credenciais inline (logos):**
- Display: flex, gap: 24px, align-items: center, margin-bottom 32px
- Logo Universidade Biohacker: imgi_3_3-3.webp, height 28px, width auto, filter: brightness(0) — fica preta
- Logo Comunidade da Longevidade: imgi_1_LOGO-1.webp, height 22px, width auto
- Separador: 1px solid --border, height 24px

**Parágrafos da bio:**
- Font: Manrope 400, 16px, line-height 1.75, color --text
- Margin-bottom: 20px entre parágrafos
- Nomes de instituições em bold (Manrope 600): "USP", "Nutrigenômica, Nutrigenética e Epigenética", "Universidade do Biohacker", "Comunidade da Longevidade", "Casa Biohacker"

**CTA:**
- Margin-top: 40px
- Mesmo estilo do hero CTA (pill verde)

### Tipografia
- **Headline:** Newsreader 700, clamp(26px, 2.8vw, 36px), line-height 1.25, letter-spacing -0.01em, color --forest
- **Headline "estratégia clínica":** `<em>` com color --cta-green, font-style italic Newsreader
- **Bio texto:** Manrope 400, 16px, line-height 1.75, color --text
- **Bio nomes/instituições:** Manrope 600, color --forest
- **Credenciais flutuantes:** Manrope 500-600, 13px, --forest
- **Logos:** filtro para preto ou manter original

### Cores
- Background: --off-white
- Texto: --text
- Nomes destacados: --forest
- Cards credenciais: rgba(255,255,255,0.92) com blur
- Headline accent: --cta-green
- Ícones credenciais: --forest

### Elementos Visuais
- Foto imgi_9_Rectangle-6697_1x.webp (Dra. Rita palestrando)
- Background blur imgi_25_BG-DKTP-1.webp
- Logo Univ. Biohacker imgi_3_3-3.webp
- Logo Comunidade Longevidade imgi_1_LOGO-1.webp
- Cards credenciais flutuantes com glassmorphism
- Ícones SVG inline: graduation cap, estrela, livro

### Animações
- **Coluna texto:** fade-up 800ms ease-out
- **Coluna visual:** fade-up 800ms ease-out, delay 100ms
- **Cards credenciais:** stagger entrance
  - Card 1: delay 300ms, fade-up
  - Card 2: delay 450ms, fade-up
  - Card 3: delay 600ms, fade-up
- **Logos:** fade-in 600ms, delay 200ms

### Interatividade
- **Cards credenciais:** float sutil permanente (keyframes float, 4-5s ease-in-out infinite, translate 0 to 0,-6px, variações por card)
- **Hover nos cards credenciais:** translateY(-3px) + shadow mais forte, 300ms ease
- **Hover na imagem:** subtle scale(1.02), 600ms ease (overflow hidden no container)

### Responsividade
**Tablet (<=960px):**
- Grid: 1fr (stack vertical)
- Visual primeiro, texto depois
- Imagem: border-radius 24px (todos os lados)
- Cards credenciais: reposicionados para dentro da imagem (não overlap)
- Coluna texto: padding-left 0, margin-top 48px
- Logos: margin-bottom 24px

**Mobile (<=600px):**
- Headline: 24px
- Imagem: border-radius 16px
- Cards credenciais: display flex horizontal (scroll se necessário), gap 12px, abaixo da imagem
- Parágrafos: 15px
- Logos height: 20px e 18px

---

## Seção 7: FAQ

### Arquétipo e Constraints
- **Arquétipo:** Contained Center (container central com margens generosas, foco no conteúdo)
- **Constraints:** Reveal on Demand (accordion) + Clip Reveal Animation + Monocromático
- **Justificativa:** FAQ precisa de clareza e legibilidade máxima. O container estreito centralizado com bastante whitespace transmite elegância e confiança. Accordion é o padrão esperado pelo usuário neste contexto (boa UX). O clip reveal animation nas respostas adiciona surpresa sutil.

### Conteúdo
- **Headline:** Perguntas frequentes

**7 perguntas:**
1. O que eu recebo exatamente na consulta?
   R: Uma consulta online de 2h, com revisão dos exames enviados, além de interpretação de teste genéticos e exames (quando necessário), prescrição, plano alimentar e um plano inicial de 30–90 dias.

2. A consulta é online?
   R: Sim. E há gravação no app.

3. Preciso ter exames antes?
   R: Não necessariamente. Se você já tiver exames recentes, você envia. Se não tiver, pode sair da consulta com interpretação de teste genéticos e exames adequado ao seu caso.

4. Essa consulta serve para perimenopausa/menopausa?
   R: Sim — é um dos contextos comuns em que a avaliação e a estratégia personalizada fazem mais diferença (sono, humor, metabolismo, sintomas).

5. E se meu objetivo for engravidar?
   R: Também pode ser contemplado: a consulta ajuda a organizar prioridades, estratégia e execução com mais clareza, conforme o seu momento.

6. Vou receber "protocolo pronto"?
   R: Você recebe um plano personalizado (alimentação + prescrição + exames + prioridades). A proposta não é encaixar você em algo genérico, e sim desenhar um caminho coerente para o seu corpo e sua rotina.

7. Isso substitui acompanhamento médico?
   R: Não. É um atendimento nutricional e de estratégia integrativa, que pode atuar em conjunto com seu médico quando necessário.

### Layout

**Desktop (>960px):**
- Background: --white
- Padding: 96px 0
- Container: max-width 720px (estreito!, centralizado)
- Padding lateral: 32px

**Headline:**
- Text-align: center
- Margin-bottom: 64px

**Accordion container:**
- Border-top: 1px solid --border

**Cada item do accordion:**
- Border-bottom: 1px solid --border
- Padding: 0

**Botão da pergunta (trigger):**
- Display: flex
- Align-items: center
- Justify-content: space-between
- Width: 100%
- Padding: 24px 0
- Background: transparent
- Border: none
- Cursor: pointer
- Text-align: left
- Gap: 16px
- Transition: color .2s ease

**Texto da pergunta:**
- Newsreader 500, 18px, line-height 1.4, color --forest

**Ícone de toggle (lado direito):**
- SVG plus/minus: 24x24px
- Stroke: --text-light, stroke-width 1.5
- Transition: transform .4s cubic-bezier(0.16, 1, 0.3, 1)
- Quando aberto: rotateZ(45deg) (o + vira x)

**Painel da resposta (colapsado por padrão):**
- Max-height: 0
- Overflow: hidden
- Transition: max-height .5s cubic-bezier(0.16, 1, 0.3, 1)
- Quando aberto: max-height calculado (ou valor seguro como 300px)

**Conteúdo da resposta (dentro do painel):**
- Padding: 0 0 24px 0
- Font: Manrope 400, 15px, line-height 1.75, color --text-light

### Tipografia
- **Headline:** Newsreader 700, clamp(28px, 3vw, 36px), line-height 1.2, color --forest, text-align center
- **Pergunta:** Newsreader 500, 18px, line-height 1.4, color --forest
- **Pergunta hover:** color --cta-green
- **Resposta:** Manrope 400, 15px, line-height 1.75, color --text-light

### Cores
- Background: --white
- Borders: --border (#E6E6E6)
- Pergunta: --forest
- Pergunta hover: --cta-green
- Pergunta ativa (aberta): --cta-green
- Ícone: --text-light, ativa --cta-green
- Resposta: --text-light

### Animações
- **Headline:** data-aos="fade-up"
- **Items:** data-aos="fade-up", stagger 50ms por item
- **Abertura da resposta:** clip-path de inset(0 0 100% 0) para inset(0), 500ms cubic-bezier(0.16, 1, 0.3, 1) — texto "desce" revelando-se
- **Ícone rotação:** transform rotateZ(0) → rotateZ(45deg), 400ms
- **Border bottom do item ativo:** color muda de --border para --mint, 300ms

### Interatividade
- **Hover na pergunta:** color muda para --cta-green, 200ms
- **Click:** abre/fecha o accordion (toggle)
- **Apenas um aberto por vez:** ao abrir um, fechar todos os outros
- **Ícone:** + quando fechado, rota 45deg (vira x) quando aberto
- **Tab focusable:** outline: 2px solid --cta-green quando focado via keyboard (outline-offset: 4px)

### Responsividade
**Mobile (<=600px):**
- Padding seção: 64px 0
- Headline: 26px
- Pergunta: 16px
- Resposta: 14px
- Padding pergunta: 20px 0
- Ícone: 20x20px

---

## Seção 8: Footer CTA (Seção final antes do popup)

### Arquétipo e Constraints
- **Arquétipo:** Single Focus (uma única coisa por seção, foco absoluto)
- **Constraints:** Gradiente Radial + Breathing Loop + Full Height (parcial)
- **Justificativa:** O CTA final precisa de impacto máximo. Uma seção focada apenas no call-to-action com background imersivo cria urgência e facilita a conversão. O breathing no CTA atrai o olhar.

### Conteúdo
- **Headline:** Sua saúde merece mais do que tentativa e erro
- **Subheadline:** Candidate-se à Consulta Nutricional Inicial com a Dra. Rita Castro e saia com um plano real para o seu corpo.
- **CTA:** QUERO ME CANDIDATAR À CONSULTA INICIAL
- **Microcopy:** Consulta online de 2h · com gravação no app

### Layout

**Desktop:**
- Background: --forest
- Padding: 96px 0
- Text-align: center
- Container: max-width 640px, centralizado

**Background decorativos:**
- Pseudo ::before: radial-gradient(circle at 50% 50%, rgba(147,218,158,0.08) 0%, transparent 60%)
- Pseudo ::after: radial-gradient(circle at 30% 70%, rgba(52,157,1,0.05) 0%, transparent 50%)

**Headline:** color --white, margin-bottom 24px
**Subheadline:** rgba(255,255,255,0.7), margin-bottom 48px, max-width 500px, margin auto
**CTA:** mesmo estilo hero (pill verde), centralizado
**Microcopy:** 13px, rgba(255,255,255,0.5), margin-top 16px

### Tipografia
- **Headline:** Newsreader 700, clamp(28px, 3.5vw, 44px), line-height 1.15, color --white
- **Subheadline:** Manrope 400, 17px, line-height 1.7, rgba(255,255,255,0.7)
- **Microcopy:** Manrope 400, 13px

### Animações
- **Headline + Subheadline:** data-aos="fade-up"
- **CTA:** breathing sutil — box-shadow pulsa (shadow normal → shadow mais larga → volta), 3s ease-in-out infinite, amplitude discreta (shadow-spread varia 2px)
- **Background gradient:** floating lento (transform translate sutil), 12s ease-in-out infinite

### Responsividade
**Mobile (<=600px):**
- Padding: 64px 0
- Headline: 28px
- Subheadline: 15px

---

## Popup - Formulário de Candidatura

### Arquétipo e Constraints
- **Arquétipo:** Modal (janela sobreposta com foco total)
- **Constraints:** Glassmorphism + Scale In Animation + Clip Reveal
- **Justificativa:** O formulário popup precisa de foco total sem distrações. Modal com overlay escuro + glassmorphism no container reforça premium. Scale-in cria uma entrada elegante.

### Conteúdo
- **Título:** Candidatura para Consulta Nutricional Inicial — Dra. Rita Castro
- **Subtítulo:** Preencha para entendermos seu momento e direcionarmos seu contato de forma objetiva.
- **Campos:**
  - Nome (text input)
  - E-mail (email input)
  - WhatsApp (tel input com intl-tel-input)
  - Qual é o seu maior desafio de saúde atual? (select: Fadiga e estresse / Desregulação hormonal feminina / Fertilidade e gestação / Doenças autoimunes / Outro)
  - Há quanto tempo isso acontece? (select: 0–6 meses / 6–12 meses / 1–3 anos / 3+ anos)
- **CTA:** ENVIAR CANDIDATURA

### Layout

**Overlay:**
- Position: fixed, inset 0
- Background: rgba(16,56,36,0.7)
- Backdrop-filter: blur(8px)
- Z-index: 1000
- Display: flex, align-items: center, justify-content: center
- Padding: 24px

**Container do popup:**
- Background: --white
- Border-radius: 24px
- Max-width: 520px
- Width: 100%
- Max-height: 90vh
- Overflow-y: auto
- Padding: 48px 40px
- Position: relative
- Box-shadow: 0 24px 80px rgba(0,0,0,0.25)

**Botão fechar (X):**
- Position: absolute, top 20px, right 20px
- Width: 36px, height: 36px
- Background: --off-white
- Border-radius: 50%
- Border: none
- Cursor: pointer
- Display: flex, align-items: center, justify-content: center
- SVG X: 18x18, stroke --text-light, stroke-width 1.5
- Hover: background --border, transition 200ms

**Título popup:**
- Newsreader 700, 24px, line-height 1.25, color --forest
- Margin-bottom: 8px

**Subtítulo popup:**
- Manrope 400, 14px, line-height 1.6, color --text-light
- Margin-bottom: 32px

**Campos de formulário:**
- Margin-bottom: 20px cada

**Label:**
- Manrope 500, 13px, color --forest, margin-bottom 6px, display block

**Input text/email:**
- Width: 100%
- Padding: 14px 16px
- Font: Manrope 400, 15px
- Color: --text
- Background: --off-white
- Border: 1px solid --border
- Border-radius: 12px
- Transition: border-color .2s ease, box-shadow .2s ease
- Focus: border-color --cta-green, box-shadow 0 0 0 3px rgba(52,157,1,0.1), outline none

**Select:**
- Mesmo estilo do input
- Appearance: none
- Background-image: chevron SVG como data URI (posição right 16px center)
- Padding-right: 40px (espaço para chevron)

**Tel input:**
- Seguir skill de forms para intl-tel-input com máscara

**CTA do formulário:**
- Width: 100%
- Padding: 18px
- Background: --cta-green
- Color: --white
- Font: Manrope 600, 15px, uppercase, letter-spacing 0.04em
- Border: none
- Border-radius: pill
- Cursor: pointer
- Margin-top: 8px
- Transition: background .25s ease, transform .25s ease, box-shadow .25s ease
- Hover: --cta-green-hover, translateY(-2px), shadow 0 6px 28px rgba(52,157,1,0.35)

### Animações
- **Overlay:** fade-in opacity 0 → 1, 300ms ease
- **Container:** scale(0.95) + opacity 0 → scale(1) + opacity 1, 400ms cubic-bezier(0.16, 1, 0.3, 1), delay 100ms
- **Fechar:** reverso das animações, 250ms ease-in
- **Campos:** stagger sutil, cada campo com delay +50ms (opacity 0 → 1, translateY(8px) → 0)

### Interatividade
- **Abrir:** todos os CTAs da página com href="#candidatura" abrem o popup
- **Fechar:** botão X, click no overlay (fora do popup), ou tecla ESC
- **Focus trap:** tab navigation limitada apenas ao popup quando aberto
- **Body scroll lock:** overflow hidden no body quando popup aberto
- **Validação inline:** border vermelha (input border #E53E3E) com mensagem sutil ao perder o foco (blur) se inválido

### Responsividade
**Mobile (<=600px):**
- Popup: border-radius 20px 20px 0 0, position fixed bottom, max-height 85vh (slide up)
- Padding: 32px 24px
- Título: 20px
- Campos padding: 12px 14px
- Animation: slide-up em vez de scale

---

## Resumo de Elementos Encantadores Planejados

### Micro-interações
- Hover lift em todos os cards com transição suave
- Linha separadora de depoimentos que expande no hover
- Ícones que fazem scale spring ao aparecer
- CTA breathing sutil no footer

### Animações Elaboradas
- Mouse parallax nos floaters do hero (já implementado)
- Imagem sticky na seção metodologia com parallax de scroll
- Cards credenciais da Dra. Rita flutuando permanentemente
- Clip-path reveal nas respostas do FAQ
- Stagger animations em todas as seções com delays calculados

### Detalhes de Craft
- Glassmorphism nos floaters do hero e cards bento
- Noise texture sutil na seção de depoimentos
- Timeline lateral com dots nos depoimentos
- Bento Box com célula vertical-span e horizontal-span
- Cards credenciais com overlap na fronteira do split

### Elementos de Surpresa
- Acordeão do FAQ que revela com clip-path (não colapso genérico)
- Números das etapas com spring animation
- Background gradientes com breathing infinito
- Popup que sobe como bottom sheet no mobile
