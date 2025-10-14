import streamlit as st
import random

# ページ設定
st.set_page_config(
    page_title="物語創作システム v2.1",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# スタイル設定
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #4A90E2;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    .trope-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
        font-size: 1.2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .request-box {
        background: linear-gradient(135deg, #a8e6cf 0%, #81c784 100%);
        color: #1b5e20;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .prompt-box {
        background: #f8f9fa;
        border: 2px solid #4A90E2;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .info-badge {
        display: inline-block;
        background: #e3f2fd;
        color: #1976d2;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.9rem;
        margin: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

# 物語要素データ - 中間トロープ
STORY_TROPES = [
    # 状況・シチュエーション系（既存10 + 追加20）
    "24時間以内に起きる出来事",
    "一つの場所から出られない状況",
    "誰かが眠り続けている",
    "全員が同じ夢を見る",
    "記憶が毎日リセットされる",
    "誰も信じてくれない真実",
    "二つの世界を行き来する",
    "時間が逆行している",
    "言葉が通じない相手との対話",
    "誰かになりすまさなければならない",
    # 追加
    "突然全ての音が消えた世界",
    "自分以外の時間が止まる瞬間",
    "全員が入れ替わっている日常",
    "重力が反転する時間帯",
    "昨日が存在しなかったことになる",
    "同じ人物が二人存在する日常",
    "鏡の中の世界との接触",
    "天候が感情に連動する",
    "影が独立して動き出す",
    "全ての嘘が真実になる一日",
    "色彩が失われていく世界",
    "物理法則が日替わりで変わる",
    "全員が透明人間になる条件",
    "夜と昼が同時に存在する",
    "重要な日が永遠に来ない",
    "季節が一日で巡る世界",
    "死者からの電話がかかってくる",
    "植物が急速に成長し続ける",
    "空が地面になる現象",
    "記録媒体から過去が消える",
    
    # 制約・ルール系（既存10 + 追加20）
    "特定の言葉を口にできない",
    "触れてはいけない存在",
    "日没までに終わらせるべきこと",
    "三つの選択肢しかない",
    "一度だけ使える力",
    "誰かの死と引き換えの願い",
    "嘘をつくと代償を払う",
    "見られてはいけない姿",
    "一人でいてはいけない理由",
    "同じことを繰り返す運命",
    # 追加
    "笑ってはいけない契約",
    "名前を呼ばれたら従う呪い",
    "三歩以上離れられない関係",
    "正午に必ず起こる出来事",
    "特定の数字を避けなければならない",
    "月光を浴びてはいけない体質",
    "質問に答えると何かを失う",
    "鏡を見ると何かが起こる",
    "七日間眠れない呪い",
    "感情を表に出すと罰を受ける",
    "右側しか見てはいけない制約",
    "毎日何かを捨てなければならない",
    "他人の名前を言えない状態",
    "境界線を越えてはいけない契約",
    "満月の夜だけ解ける呪い",
    "血を流してはいけない約束",
    "誰かの許可なく動けない",
    "音を立てると消える存在",
    "五感のうち一つを捧げた代償",
    "完璧でなければ消滅する運命",
    
    # 関係性の動態系（既存10 + 追加20）
    "互いの正体を隠している二人",
    "一方的に記憶されている関係",
    "敵同士が協力せざるを得ない",
    "保護者と被保護者の逆転",
    "血縁の嘘",
    "師弟関係の終焉",
    "代理として生きる人生",
    "監視する者と監視される者",
    "依存と支配の境界",
    "世代を超えた約束の継承",
    # 追加
    "互いが互いの過去である関係",
    "感情が同期してしまう二人",
    "片方にしか見えない相手",
    "役割が定期的に入れ替わる",
    "距離が近づくほど苦痛を伴う",
    "記憶を共有する宿命",
    "一方が老いず一方が老いる",
    "言葉なしでしか理解できない絆",
    "互いの死が条件の共生",
    "過去の自分との出会い",
    "並行世界の自分との接触",
    "親子関係の時系列崩壊",
    "敵だった者が唯一の味方",
    "存在を認識されない関係",
    "感情の吸血鬼とその宿主",
    "運命を交換した二人",
    "一方の幸福が他方の不幸",
    "記憶の中でしか会えない関係",
    "互いが互いの創造主",
    "憎しみでしか繋がれない絆",
    
    # 能力・条件系（既存10 + 追加20）
    "他人の感情が分かってしまう",
    "未来が断片的に見える",
    "死者の声が聞こえる",
    "特定の人物だけに見える存在",
    "感情を失った代わりに得たもの",
    "誰かの代わりに苦痛を受ける",
    "真実を見抜く目",
    "触れたものの過去が分かる",
    "一つだけ時間を戻せる力",
    "他人の人生を体験する夢",
    # 追加
    "他人の寿命が見える目",
    "願いが必ず悪い形で叶う",
    "痛みを感じない代償",
    "他人の夢に侵入できる",
    "嘘が物理的に発声できない",
    "死んだ後も意識が残る",
    "一日だけ他人になれる",
    "触れたものを修復できる",
    "自分の存在を消せる力",
    "他人の記憶を書き換える",
    "植物と会話できる能力",
    "影を操る力",
    "過去の自分に手紙を送れる",
    "運命の分岐点が視覚化される",
    "他人の秘密が自動的に分かる",
    "物質を一つだけ生成できる",
    "重要な瞬間が予告される",
    "感情が色として見える",
    "死の瞬間を何度も体験する",
    "平行世界の自分の記憶が流入",
    
    # 場所・空間の性質系（既存10 + 追加20）
    "時間の流れが異なる場所",
    "入るたびに変化する空間",
    "現実と幻想の境界が曖昧な場所",
    "過去の記憶が再現される場所",
    "禁忌を破った者だけが見える世界",
    "生者と死者が交わる場所",
    "二つの時代が重なる地点",
    "真実だけが響く部屋",
    "感情が具現化する空間",
    "全ての終わりが始まる場所",
    # 追加
    "願いを必ず奪う部屋",
    "入った者が別人になる建物",
    "時系列が逆転する廊下",
    "音が視覚化される空間",
    "重力の存在しない地帯",
    "記憶が物質化する場所",
    "感情が天候になる領域",
    "全ての鏡が繋がる空間",
    "言葉が実体化する部屋",
    "過去の選択が再現される交差点",
    "夢と現実が融合する境界",
    "存在が薄れていく地帯",
    "時間が止まったままの家",
    "人格が分裂する空間",
    "罪が可視化される法廷",
    "全ての可能性が同時存在する点",
    "死者の最期が再生される場所",
    "感覚が入れ替わる部屋",
    "因果律が崩壊した領域",
    "記録が改変される図書館",
    
    # 心理・認識系（既存10 + 追加20）
    "自分が本物か分からない",
    "他人の記憶を持っている",
    "二つの人格の共存",
    "過去の自分と対峙する",
    "自分の死を予知している",
    "他人から見た自分を知る",
    "現実と虚構の区別がつかない",
    "重要な何かを忘れている確信",
    "誰かの記憶の中で生きている",
    "存在しなかったことにされた人生",
    # 追加
    "自分が創作物だと気づく",
    "他人の意識が混入している",
    "過去の改変を覚えている唯一人",
    "自分が既に死んでいる可能性",
    "全ての経験が追体験だった",
    "現実が誰かの夢だと知る",
    "自分の目的を思い出せない",
    "人格が日替わりで変わる",
    "他者の視点で自分を観察できる",
    "アイデンティティが流動的",
    "過去と現在の自分が別人",
    "存在証明ができない状態",
    "感情が他人のものだと気づく",
    "自由意志が幻想だと知る",
    "自分が複製品である証拠",
    "記憶が全て偽造されている",
    "意識が複数の体に分散",
    "自我が徐々に消失していく",
    "他人の人生を生きている自覚",
    "現実が書き換わる瞬間を認識",
    
    # 時間・タイミング系（既存10 + 追加20）
    "運命の分岐点への回帰",
    "あと一度だけ会える機会",
    "過去が変更された現在",
    "決められた順序でしか起きない出来事",
    "誰かの時間を奪って生きる",
    "特定の瞬間だけ発動する力",
    "過去の選択のやり直し",
    "未来の自分からのメッセージ",
    "時間制限付きの命",
    "永遠に繰り返される一日",
    # 追加
    "過去と未来が同時に見える",
    "寿命が可視化されたカウンター",
    "時間の流れが個人ごとに違う",
    "特定の瞬間に戻り続ける",
    "時系列がランダムに体験される",
    "老化が逆転する現象",
    "未来の後悔が現在に届く",
    "時間が通貨として扱われる",
    "死ぬ瞬間が事前に通知される",
    "過去の自分に干渉できる一度",
    "全ての時間軸が収束する時",
    "時間が人によって違う速度",
    "未来が過去を変更する",
    "残り時間だけが表示される",
    "時間の借金を抱えた人生",
    "永遠の五分間を生きる",
    "時間旅行の痕跡が残る体",
    "複数の時間軸を同時に生きる",
    "時の流れから外れた存在",
    "最期の一日を何度も繰り返す",
    
    # 新規：変化・変容系（20個）
    "徐々に別の生物になっていく",
    "感情が身体を変化させる",
    "言葉を失うたびに何かを得る",
    "人間性を代償に力を得る",
    "形を保てなくなる身体",
    "他者の特徴を吸収する体質",
    "段階的に透明になる呪い",
    "声が他人のものになっていく",
    "物質と意識の境界崩壊",
    "人間から概念へ変わる過程",
    "季節ごとに別人格になる",
    "接触した相手に同化する",
    "記憶を失う代わりに進化する",
    "感覚が一つずつ消えていく",
    "実体から情報へと変質する",
    "二つの存在が融合していく",
    "元の姿を忘れた変身者",
    "完全になる前に朽ちる定め",
    "人間性の段階的喪失",
    "存在形態が不安定な生命",
    
    # 新規：知覚・感覚系（20個）
    "他人の痛みを感じる共感覚",
    "全ての音楽が悲鳴に聞こえる",
    "色が感情として知覚される",
    "文字が立体として見える",
    "味覚で過去を追体験する",
    "触覚だけで世界を認識する",
    "匂いで嘘を見抜く能力",
    "時間が物理的に感じられる",
    "他人の視界が見える目",
    "感情が音として聞こえる",
    "距離感覚が崩壊した認識",
    "全ての物体から声が聞こえる",
    "温度で記憶を読み取る",
    "影に別の世界が見える",
    "シンクロニシティが視覚化",
    "危機が味として警告される",
    "空間の歪みを感じる感覚",
    "他者の思考が香りになる",
    "感覚が時差を持って届く",
    "五感の優先順位が日替わり",
    
    # 新規：存在・実存系（20個）
    "観測されない時の自分が別人",
    "他者の認識で姿が変わる",
    "信じられなくなると消える",
    "忘れられると死ぬ運命",
    "名前を奪われた存在",
    "影だけが残った人間",
    "概念として生きる元人間",
    "誰の記憶にも残らない人生",
    "存在の証明を求め続ける",
    "他人に見られて初めて存在する",
    "複数の現実に同時存在",
    "実在と虚構の狭間",
    "自己言及で消滅する危機",
    "他者の想像の産物として生きる",
    "存在理由を探す旅",
    "現象としてのみ残る意識",
    "誰かの夢から出られない",
    "物語の登場人物としての自覚",
    "観測者なき世界の住人",
    "存在の優先度が低い者",
]

# セッション状態の初期化
if 'trope1' not in st.session_state:
    st.session_state.trope1 = None
if 'trope2' not in st.session_state:
    st.session_state.trope2 = None

# ヘッダー
st.markdown('<h1 class="main-header">📚 物語創作システム v2.1</h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #666; margin-bottom: 2rem;">🎲 意外性を生む中間トロープの組み合わせ</div>', unsafe_allow_html=True)

# サイドバー
with st.sidebar:
    st.header("🎲 ランダム生成")
    
    if st.button("2つのトロープを生成", type="primary", use_container_width=True):
        # 重複しないように2つ選択
        selected = random.sample(STORY_TROPES, 2)
        st.session_state.trope1 = selected[0]
        st.session_state.trope2 = selected[1]
        st.success("✅ トロープを生成しました!")
        st.rerun()
    
    st.divider()
    
    st.header("📊 選択状況")
    if st.session_state.trope1:
        st.success(f"✅ トロープ1:\n{st.session_state.trope1}")
    else:
        st.error("❌ トロープ1: 未選択")
    
    if st.session_state.trope2:
        st.success(f"✅ トロープ2:\n{st.session_state.trope2}")
    else:
        st.error("❌ トロープ2: 未選択")
    
    st.divider()
    
    st.markdown("""
    <div style="font-size: 0.85rem; color: #666;">
    <strong>💡 ヒント</strong><br>
    中間トロープの組み合わせで、<br>
    予測不可能な物語が生まれます
    </div>
    """, unsafe_allow_html=True)

# メインコンテンツ
st.header("🎯 トロープ選択")

col1, col2 = st.columns(2)

# トロープ1
with col1:
    st.subheader("トロープ 1")
    
    if st.button("🎯 ランダム選択", key="random_trope1", use_container_width=True):
        # トロープ2と重複しないように選択
        available = [t for t in STORY_TROPES if t != st.session_state.trope2]
        st.session_state.trope1 = random.choice(available)
        st.rerun()
    
    if st.session_state.trope1:
        st.markdown(f'<div class="trope-box">{st.session_state.trope1}</div>', unsafe_allow_html=True)
    else:
        st.info("「ランダム選択」ボタンを押してください")

# トロープ2
with col2:
    st.subheader("トロープ 2")
    
    if st.button("🎯 ランダム選択", key="random_trope2", use_container_width=True):
        # トロープ1と重複しないように選択
        available = [t for t in STORY_TROPES if t != st.session_state.trope1]
        st.session_state.trope2 = random.choice(available)
        st.rerun()
    
    if st.session_state.trope2:
        st.markdown(f'<div class="trope-box">{st.session_state.trope2}</div>', unsafe_allow_html=True)
    else:
        st.info("「ランダム選択」ボタンを押してください")

# 追加リクエストセクション
st.divider()
st.header("💬 追加リクエスト（任意）")
user_request = st.text_area(
    "",
    placeholder="例：既存キャラクター「◯◯」を使用、特定の雰囲気にしたい、長さの指定など...",
    height=100,
    key="user_request"
)

if user_request:
    st.markdown(f'<div class="request-box"><strong>追加リクエスト:</strong><br>{user_request}</div>', unsafe_allow_html=True)

# プロンプト生成
st.divider()
st.header("🎭 物語プロンプト生成")

all_tropes_selected = st.session_state.trope1 and st.session_state.trope2

if st.button("📝 物語プロンプト生成", type="primary", disabled=not all_tropes_selected, use_container_width=True):
    request_section = ""
    if user_request.strip():
        request_section = f"\n\n## 追加リクエスト\n{user_request.strip()}"
    
    tropes_text = f"""1. **「{st.session_state.trope1}」**
2. **「{st.session_state.trope2}」**
"""
    
    prompt = f"""# 短編物語創作依頼

## 使用するトロープ（物語要素）
{tropes_text}
## 登場人物設定
**指示**: 選択されたトロープに最も適した魅力的なキャラクター（1人以上）を、AIが自由に設定してください。名前はユニークなものにしてください。「美咲」は禁止です。年代、職業、性格などを物語のテーマに合わせて選択し、読者が感情移入しやすいキャラクターを作成してください。{request_section}

## 創作指示
上記の2つのトロープを自然に組み合わせた短編小説を創作してください。
- 両方のトロープが物語に有機的に統合されているようにしてください
- トロープ同士の意外な組み合わせから生まれる独創性を活かしてください
- 文字数制限はありません（自然な長さで完結させてください）
- 読者が引き込まれる魅力的な物語に仕上げてください
- 意外性のある展開や結末を心がけてください"""
    
    st.markdown('<div class="prompt-box">', unsafe_allow_html=True)
    st.markdown("### 📋 生成されたプロンプト")
    st.code(prompt, language="markdown")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.text_area("コピー用（全選択してコピーしてください）", prompt, height=200)
    
    st.success("✅ プロンプトが生成されました！上記をコピーしてClaudeに送信してください。")
    
    # トロープの組み合わせ情報
    st.info(f"🎲 **今回の組み合わせ**: 「{st.session_state.trope1}」×「{st.session_state.trope2}」")

if not all_tropes_selected:
    st.warning("⚠️ 2つのトロープを選択してください。")

# フッター
st.divider()
st.markdown(f"""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    📚 物語創作システム v2.1 - 中間トロープ組み合わせ版<br>
    <span class="info-badge">トロープ総数: {len(STORY_TROPES)}個</span>
    <span class="info-badge">可能な組み合わせ: {len(STORY_TROPES) * (len(STORY_TROPES) - 1) // 2}通り</span>
</div>
""", unsafe_allow_html=True)
