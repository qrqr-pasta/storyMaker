import streamlit as st
import random

# ページ設定
st.set_page_config(
    page_title="物語創作システム",
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
    .element-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    .element-box-none {
        background: linear-gradient(135deg, #95a5a6 0%, #7f8c8d 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin: 0.5rem 0;
        font-style: italic;
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
    .stSelectbox > div > div {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 物語要素データ（リファイン版）
STORY_ELEMENTS = {
    # Layer1: 物語の基本構造（プロット・アーキタイプ）
    "layer1": [
        # 探索・発見系
        "失われたものを探す旅", "禁じられた場所への侵入", "隠された真実の発見",
        "忘れられた過去の発掘", "未知の世界への冒険", "謎の解明",
        
        # 対立・葛藤系
        "復讐の連鎖", "裏切りと報復", "善と悪の対決", "権力への反逆",
        "不可能への挑戦", "運命との戦い", "時間制限のある危機",
        
        # 変容・成長系
        "無名から英雄へ", "堕落と redemption", "アイデンティティの喪失と再構築",
        "師との別れと独り立ち", "罪と赦し", "絶望からの再生",
        
        # 関係性の変化
        "禁断の愛", "失った人との再会", "敵から味方へ", "信頼の崩壊",
        "世代を超えた対話", "運命的な出会い",
        
        # 犠牲と選択
        "大切なものとの別れ", "究極の選択", "誰かのための犠牲",
        "守るべきものの喪失", "取り返しのつかない決断",
        
        # その他
        "入れ替わる人生", "繰り返される悪夢", "予言の成就", "因果応報"
    ],
    
    # Layer2: テクスチャを与える小道具（象徴・モチーフ）
    "layer2": [
        # 記憶・記録を繋ぐもの
        "色褪せた手紙", "破れた日記", "古い写真", "録音テープ",
        "血で書かれた遺言", "暗号化された地図", "消えかけの刺繍",
        
        # 時間を象徴するもの
        "止まった時計", "砂時計", "朽ちた暦", "季節外れの花",
        "風化した墓標", "錆びた鍵",
        
        # 約束・契約の象徴
        "割れた指輪", "半分のペンダント", "対の剣", "結ばれた赤い糸",
        "封印された契約書", "欠けた勲章",
        
        # 身体・生命に関わるもの
        "消えない傷跡", "失われた記憶", "奪われた声", "見えない目",
        "凍った涙", "流れない血", "震える手",
        
        # 自然現象・天候
        "降り続く雨", "止まない雷鳴", "消えない霧", "永遠の夕暮れ",
        "真夜中の虹", "満月の夜", "血の色の雪",
        
        # 動物・生き物
        "片翼の鳥", "二度鳴く烏", "白い獣", "導く蝶",
        "不吉な黒猫", "人語を話す魚", "影の犬",
        
        # 音・音楽
        "聞こえない旋律", "不協和音", "子守唄", "鐘の音",
        "壊れたオルゴール", "最後の歌声",
        
        # 場所・空間
        "閉ざされた扉", "壊れた橋", "枯れた井戸", "忘れられた庭",
        "境界線", "鏡の向こう", "夢と現実の狭間",
        
        # 抽象概念の具現化
        "影の取引", "嘘の代償", "沈黙の誓い", "呪われた才能",
        "盗まれた名前", "売られた魂", "失われた笑顔"
    ]
}

# セッション状態の初期化
if 'elements' not in st.session_state:
    st.session_state.elements = {
        'layer1': None,
        'layer2': None
    }

# ヘッダー
st.markdown('<h1 class="main-header">📚 物語創作システム</h1>', unsafe_allow_html=True)

# サイドバー
with st.sidebar:
    st.header("🎲 クイック操作")
    
    if st.button("すべてランダム生成", type="primary", use_container_width=True):
        # 全要素をランダム選択（「選ばない」は含まない）
        for layer in STORY_ELEMENTS:
            st.session_state.elements[layer] = random.choice(STORY_ELEMENTS[layer])
        
        st.success("✅ 全要素をランダム生成しました!")
        st.rerun()
    
    # 個別ランダム選択
    st.subheader("🎯 個別ランダム選択")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔀 劇的状況", use_container_width=True):
            st.session_state.elements['layer1'] = random.choice(STORY_ELEMENTS['layer1'])
            st.rerun()
    
    with col2:
        if st.button("🔀 装飾・関係性", use_container_width=True):
            st.session_state.elements['layer2'] = random.choice(STORY_ELEMENTS['layer2'])
            st.rerun()

    st.divider()
    
    st.header("📊 選択状況")
    for layer, label in [
        ('layer1', '劇的状況'),
        ('layer2', '装飾・関係性')
    ]:
        if st.session_state.elements[layer]:
            if st.session_state.elements[layer] == "選ばない":
                st.info(f"⚪ {label}: {st.session_state.elements[layer]}")
            else:
                st.success(f"✅ {label}: {st.session_state.elements[layer]}")
        else:
            st.error(f"❌ {label}")

# メインコンテンツ
st.header("🎯 物語要素選択")

# 2つの要素を1x2で配置
row1_col1, row1_col2 = st.columns(2)

columns = [row1_col1, row1_col2]
layers = [
    ('layer1', '第1層（劇的状況）'),
    ('layer2', '第2層（装飾・関係性）')
]

for i, (layer, label) in enumerate(layers):
    with columns[i]:
        st.subheader(label)
        
        # ドロップダウンで選択
        options = ["選択してください..."] + ["選ばない"] + STORY_ELEMENTS[layer]
        current_index = 0
        if st.session_state.elements[layer]:
            try:
                current_index = options.index(st.session_state.elements[layer])
            except ValueError:
                current_index = 0
        
        selected = st.selectbox(
            "",
            options,
            index=current_index,
            key=f"select_{layer}"
        )
        
        if selected != "選択してください...":
            st.session_state.elements[layer] = selected
        elif selected == "選択してください..." and current_index != 0:
            st.session_state.elements[layer] = None
        
        # ランダム選択ボタン（常に表示）
        if st.button(f"🎯 ランダム選択", key=f"random_{layer}", use_container_width=True):
            st.session_state.elements[layer] = random.choice(STORY_ELEMENTS[layer])
            st.rerun()
        
        # 選択された要素を表示
        if st.session_state.elements[layer]:
            if st.session_state.elements[layer] == "選ばない":
                st.markdown(f'<div class="element-box-none">この要素は使用しない</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="element-box">{st.session_state.elements[layer]}</div>', unsafe_allow_html=True)
        else:
            st.info("要素を選択してください")

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

# 生成可能かチェック
all_elements_selected = all(st.session_state.elements[layer] is not None for layer in st.session_state.elements)

if st.button("📝 物語プロンプト生成", type="primary", disabled=not all_elements_selected, use_container_width=True):
    # プロンプト生成
    request_section = ""
    if user_request.strip():
        request_section = f"\n\n## 追加リクエスト\n{user_request.strip()}"
    
    # 選ばれた要素のみをプロンプトに含める
    elements_text = ""
    element_count = 1
    
    if st.session_state.elements['layer1'] != "選ばない":
        elements_text += f"{element_count}. **「{st.session_state.elements['layer1']}」** (第1層（劇的状況）)\n"
        element_count += 1
    
    if st.session_state.elements['layer2'] != "選ばない":
        elements_text += f"{element_count}. **「{st.session_state.elements['layer2']}」** (第2層（装飾・関係性）)\n"
        element_count += 1
    
    # 全ての要素が「選ばない」の場合の処理
    if elements_text == "":
        elements_text = "**注意**: すべての要素が「選ばない」に設定されています。自由な発想で物語を創作してください。\n"
        creation_instruction = "自由な発想で魅力的な短編小説を創作してください。"
    else:
        creation_instruction = "上記の物語要素をすべて含む短編小説を創作してください。"
    
    prompt = f"""# 短編物語創作依頼

## 使用する物語要素
{elements_text}
## 登場人物設定
**指示**: 選択された物語要素に最も適した魅力的なキャラクター（1人以上）を、AIが自由に設定してください。年代、職業、性格などを物語のテーマに合わせて選択し、読者が感情移入しやすいキャラクターを作成してください。{request_section}

## 創作指示
{creation_instruction}
- 各要素は自然に物語に組み込んでください
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
    
    # コピー用テキストエリア
    st.text_area("コピー用（全選択してコピーしてください）", prompt, height=200)
    
    st.success("✅ プロンプトが生成されました！上記をコピーしてClaudeに送信してください。")

if not all_elements_selected:
    st.warning(f"⚠️ 物語要素を選択してください。")

# フッター
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    📚 物語創作システム - Claude × Streamlit版
</div>
""", unsafe_allow_html=True)
