import streamlit as st
import random

# ページ設定
st.set_page_config(
    page_title="物語創作システム v3",
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

# 物語要素データ - 全トロープ統合版(145個)
STORY_TROPES = [
    # 物語類型(15個)
    "ヒーローズジャーニー(英雄の旅)",
    "探索・クエスト",
    "立身出世",
    "航海と帰還",
    "悲劇(破滅への道)",
    "再生・復活",
    "怪物退治",
    "謎解き・探偵",
    "復讐譚",
    "救済・贖罪",
    "恋愛成就",
    "成長・通過儀礼",
    "反乱・革命",
    "喪失と受容",
    "運命との対決",
    
    # 上位トロープ(10個)
    "正義対悪",
    "秩序対混沌",
    "個人対社会",
    "自由対束縛",
    "真実対虚偽",
    "生対死",
    "変化対不変",
    "内面対外面",
    "希望対絶望",
    "自然対人工",
    
    # 中間トロープ - 状況・シチュエーション系(10個)
    "24時間以内に起きる出来事",
    "一つの場所から出られない状況",
    "記憶が毎日リセットされる",
    "二つの世界を行き来する",
    "時間が逆行している",
    "言葉が通じない相手との対話",
    "全員が同じ夢を見る",
    "誰も信じてくれない真実",
    "影が独立して動き出す",
    "物理法則が日替わりで変わる",
    
    # 中間トロープ - 制約・ルール系(10個)
    "特定の言葉を口にできない",
    "触れてはいけない存在",
    "日没までに終わらせるべきこと",
    "一度だけ使える力",
    "誰かの死と引き換えの願い",
    "嘘をつくと代償を払う",
    "同じことを繰り返す運命",
    "名前を呼ばれたら従う呪い",
    "満月の夜だけ解ける呪い",
    "五感のうち一つを捧げた代償",
    
    # 中間トロープ - 関係性の動態系(10個)
    "互いの正体を隠している二人",
    "敵同士が協力せざるを得ない",
    "一方的に記憶されている関係",
    "代理として生きる人生",
    "世代を超えた約束の継承",
    "感情が同期してしまう二人",
    "片方にしか見えない相手",
    "互いの死が条件の共生",
    "記憶を共有する宿命",
    "憎しみでしか繋がれない絆",
    
    # 中間トロープ - 能力・条件系(10個)
    "他人の感情が分かってしまう",
    "未来が断片的に見える",
    "死者の声が聞こえる",
    "誰かの代わりに苦痛を受ける",
    "真実を見抜く目",
    "一つだけ時間を戻せる力",
    "願いが必ず悪い形で叶う",
    "他人の記憶を書き換える",
    "自分の存在を消せる力",
    "平行世界の自分の記憶が流入",
    
    # 中間トロープ - 場所・空間の性質系(10個)
    "時間の流れが異なる場所",
    "入るたびに変化する空間",
    "現実と幻想の境界が曖昧な場所",
    "生者と死者が交わる場所",
    "真実だけが響く部屋",
    "感情が具現化する空間",
    "時系列が逆転する廊下",
    "記憶が物質化する場所",
    "因果律が崩壊した領域",
    "全ての可能性が同時存在する点",
    
    # 中間トロープ - 心理・認識系(10個)
    "自分が本物か分からない",
    "他人の記憶を持っている",
    "二つの人格の共存",
    "現実と虚構の区別がつかない",
    "重要な何かを忘れている確信",
    "存在しなかったことにされた人生",
    "自分が創作物だと気づく",
    "過去の改変を覚えている唯一人",
    "自由意志が幻想だと知る",
    "自我が徐々に消失していく",
    
    # 中間トロープ - 時間・タイミング系(10個)
    "運命の分岐点への回帰",
    "あと一度だけ会える機会",
    "誰かの時間を奪って生きる",
    "特定の瞬間だけ発動する力",
    "未来の自分からのメッセージ",
    "時間制限付きの命",
    "永遠に繰り返される一日",
    "時間が通貨として扱われる",
    "時間の流れから外れた存在",
    "複数の時間軸を同時に生きる",
    
    # 中間トロープ - 変化・変容系(10個)
    "徐々に別の生物になっていく",
    "感情が身体を変化させる",
    "人間性を代償に力を得る",
    "他者の特徴を吸収する体質",
    "人間から概念へ変わる過程",
    "接触した相手に同化する",
    "記憶を失う代わりに進化する",
    "感覚が一つずつ消えていく",
    "二つの存在が融合していく",
    "存在形態が不安定な生命",
    
    # 中間トロープ - 知覚・感覚系(10個)
    "他人の痛みを感じる共感覚",
    "色が感情として知覚される",
    "味覚で過去を追体験する",
    "匂いで嘘を見抜く能力",
    "時間が物理的に感じられる",
    "感情が音として聞こえる",
    "距離感覚が崩壊した認識",
    "全ての物体から声が聞こえる",
    "シンクロニシティが視覚化",
    "感覚が時差を持って届く",
    
    # 中間トロープ - 存在・実存系(10個)
    "観測されない時の自分が別人",
    "忘れられると死ぬ運命",
    "名前を奪われた存在",
    "概念として生きる元人間",
    "誰の記憶にも残らない人生",
    "他人に見られて初めて存在する",
    "複数の現実に同時存在",
    "他者の想像の産物として生きる",
    "物語の登場人物としての自覚",
    "存在の優先度が低い者",
    
    # 下位トロープ - 小道具・モチーフ(20個)
    "猫",
    "犬",
    "鳥",
    "鼠",
    "兎",
    "蝶",
    "蟻",
    "バッグ",
    "鍵",
    "鏡",
    "時計",
    "写真",
    "扉",
    "本",
    "手紙",
    "階段",
    "羽根",
    "仮面",
    "楽器",
    "花",
    "月",
    "雨",
    "影",
]

# セッション状態の初期化
if 'trope1' not in st.session_state:
    st.session_state.trope1 = None
if 'trope2' not in st.session_state:
    st.session_state.trope2 = None

# ヘッダー
st.markdown('<h1 class="main-header">📚 物語創作システム v3</h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #666; margin-bottom: 2rem;">🎲 4層トロープ統合版 - 類型・上位・中間・下位すべてをフラットに選択</div>', unsafe_allow_html=True)

# サイドバー
with st.sidebar:
    st.header("🎲 ランダム生成")
    
    if st.button("2つのトロープを生成", type="primary", use_container_width=True):
        # 重複を許して2つ選択
        st.session_state.trope1 = random.choice(STORY_TROPES)
        st.session_state.trope2 = random.choice(STORY_TROPES)
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
    物語類型、上位対立、中間設定、<br>
    小道具まで、あらゆる層からの<br>
    組み合わせで新しい物語が生まれます
    </div>
    """, unsafe_allow_html=True)

# メインコンテンツ
st.header("🎯 トロープ選択")

col1, col2 = st.columns(2)

# トロープ1
with col1:
    st.subheader("トロープ 1")
    
    if st.button("🎯 ランダム選択", key="random_trope1", use_container_width=True):
        st.session_state.trope1 = random.choice(STORY_TROPES)
        st.rerun()
    
    if st.session_state.trope1:
        st.markdown(f'<div class="trope-box">{st.session_state.trope1}</div>', unsafe_allow_html=True)
    else:
        st.info("「ランダム選択」ボタンを押してください")

# トロープ2
with col2:
    st.subheader("トロープ 2")
    
    if st.button("🎯 ランダム選択", key="random_trope2", use_container_width=True):
        st.session_state.trope2 = random.choice(STORY_TROPES)
        st.rerun()
    
    if st.session_state.trope2:
        st.markdown(f'<div class="trope-box">{st.session_state.trope2}</div>', unsafe_allow_html=True)
    else:
        st.info("「ランダム選択」ボタンを押してください")

# 追加リクエストセクション
st.divider()
st.header("💬 追加リクエスト(任意)")
user_request = st.text_area(
    "",
    placeholder="例:既存キャラクター「◯◯」を使用、特定の雰囲気にしたい、長さの指定など...",
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

## 使用するトロープ(物語要素)
{tropes_text}
## 登場人物設定
**指示**: 選択されたトロープに最も適した魅力的なキャラクター(1人以上)を、AIが自由に設定してください。年代、職業、性格などを物語のテーマに合わせて選択し、読者が感情移入しやすいキャラクターを作成してください。固有名詞は重複を避けるために一般的でない名前にしてください。特に”美咲”は頻出する傾向なので、禁止します。{request_section}

## 創作指示
上記の2つのトロープを自然に組み合わせた短編小説を創作してください。
- 両方のトロープが物語に有機的に統合されているようにしてください
- トロープ同士の意外な組み合わせから生まれる独創性を活かしてください
- 文字数制限はありません(自然な長さで完結させてください)
- 読者が引き込まれる魅力的な物語に仕上げてください
- 意外性のある展開や結末を心がけてください"""
    
    st.markdown('<div class="prompt-box">', unsafe_allow_html=True)
    st.markdown("### 📋 生成されたプロンプト")
    st.code(prompt, language="markdown")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.text_area("コピー用(全選択してコピーしてください)", prompt, height=200)
    
    st.success("✅ プロンプトが生成されました!上記をコピーしてClaudeに送信してください。")
    
    # トロープの組み合わせ情報
    st.info(f"🎲 **今回の組み合わせ**: 「{st.session_state.trope1}」×「{st.session_state.trope2}」")

if not all_tropes_selected:
    st.warning("⚠️ 2つのトロープを選択してください。")

# フッター
st.divider()
st.markdown(f"""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    📚 物語創作システム v3 - 4層トロープ統合版<br>
    <span class="info-badge">トロープ総数: {len(STORY_TROPES)}個</span>
    <span class="info-badge">物語類型: 15個</span>
    <span class="info-badge">上位対立: 10個</span>
    <span class="info-badge">中間設定: 100個</span>
    <span class="info-badge">小道具: 20個</span>
</div>
""", unsafe_allow_html=True)
