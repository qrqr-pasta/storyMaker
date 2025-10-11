import streamlit as st
import random

# ページ設定
st.set_page_config(
    page_title="物語創作システム v2",
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
    # 状況・シチュエーション系
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
    
    # 制約・ルール系
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
    
    # 関係性の動態系
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
    
    # 能力・条件系
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
    
    # 場所・空間の性質系
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
    
    # 心理・認識系
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
    
    # 時間・タイミング系
    "運命の分岐点への回帰",
    "あと一度だけ会える機会",
    "過去が変更された現在",
    "決められた順序でしか起きない出来事",
    "誰かの時間を奪って生きる",
    "特定の瞬間だけ発動する力",
    "過去の選択のやり直し",
    "未来の自分からのメッセージ",
    "時間制限付きの命",
    "永遠に繰り返される一日"
]

# セッション状態の初期化
if 'trope1' not in st.session_state:
    st.session_state.trope1 = None
if 'trope2' not in st.session_state:
    st.session_state.trope2 = None

# ヘッダー
st.markdown('<h1 class="main-header">📚 物語創作システム v2</h1>', unsafe_allow_html=True)
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
**指示**: 選択されたトロープに最も適した魅力的なキャラクター（1人以上）を、AIが自由に設定してください。年代、職業、性格などを物語のテーマに合わせて選択し、読者が感情移入しやすいキャラクターを作成してください。{request_section}

## 創作指示
上記の2つのトロープを自然に組み合わせた短編小説を創作してください。
- 両方のトロープが物語に有機的に統合されているようにしてください
- トロープ同士の意外な組み合わせから生まれる独創性を活かしてください
- 文字数制限はありません（自然な長さで完結させてください）
- 読者が引き込まれる魅力的な物語に仕上げてください
- 意外性のある展開や結末を心がけてください

## 改善プロンプト依頼
物語作成後、以下を追加で提供してください：
**「この作品をより良くするための改善プロンプト」**
- 作品の良い点と改善すべき点を分析
- 具体的な改善指示を含む新しいプロンプトを生成
- そのプロンプトで再作成すれば、より魅力的な作品になるような内容で"""
    
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
    📚 物語創作システム v2 - 中間トロープ組み合わせ版<br>
    <span class="info-badge">トロープ総数: {len(STORY_TROPES)}個</span>
    <span class="info-badge">可能な組み合わせ: {len(STORY_TROPES) * (len(STORY_TROPES) - 1) // 2}通り</span>
</div>
""", unsafe_allow_html=True)
