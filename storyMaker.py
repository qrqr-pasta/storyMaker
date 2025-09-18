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
    .character-box {
        background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
        color: #2d3436;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        font-weight: bold;
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

# 物語要素データ
STORY_ELEMENTS = {
    "layer1": ["救助", "復讐", "逃走", "誘拐", "競争", "謎解き", "裏切り", "犠牲", "守護", "探索", "決闘", "追跡", "潜入", "破壊", "創造", "治療", "教育", "説得", "交渉", "建設", "発見", "発明", "改革", "革命", "再生", "覚醒", "継承", "伝承", "成長", "変化"],
    
    "layer2": ["双子", "師弟関係", "三角関係", "幼馴染", "手紙", "日記", "猫", "約束", "秘密", "時計", "指輪", "剣", "本", "鏡", "写真", "音楽", "絵画", "花", "星", "月", "雨", "雪", "風", "雷", "光", "影", "扉", "鍵", "地図", "宝石", "羽根", "翼", "角", "尻尾", "マント", "帽子", "仮面", "タトゥー", "傷跡", "記憶の欠片", "魔法の杖", "クリスタル", "オルゴール", "懐中時計", "ペンダント", "ブレスレット", "イヤリング", "香水", "薬", "毒", "解毒剤", "魔法の薬", "愛の薬", "記憶の薬", "変身の薬", "透明の薬", "力の薬", "治癒の薬"]
}

AGES = ["10代", "20代", "30代", "40代", "50代", "60代以上"]
JOBS = ["学生", "教師", "医者", "エンジニア", "芸術家", "警察官", "研究者", "商人", "農家", "作家", "パイロット", "料理人", "弁護士", "記者", "探偵"]
PERSONALITIES = ["楽観的", "悲観的", "情熱的", "冷静", "好奇心旺盛", "慎重", "行動的", "内向的", "外向的", "完璧主義", "自由奔放", "責任感が強い"]

# セッション状態の初期化
if 'elements' not in st.session_state:
    st.session_state.elements = {
        'layer1': None,
        'layer2': None
    }

if 'character_mode' not in st.session_state:
    st.session_state.character_mode = None

if 'characters' not in st.session_state:
    st.session_state.characters = None

# ヘッダー
st.markdown('<h1 class="main-header">📚 物語創作システム</h1>', unsafe_allow_html=True)

# サイドバー
with st.sidebar:
    st.header("🎲 クイック操作")
    
    if st.button("すべてランダム生成", type="primary", use_container_width=True):
        # 全要素をランダム選択（選ばない選択肢も含む）
        for layer in STORY_ELEMENTS:
            # ランダムで「選ばない」か要素を選択（20%の確率で「選ばない」）
            if random.random() < 0.2:
                st.session_state.elements[layer] = "選ばない"
            else:
                st.session_state.elements[layer] = random.choice(STORY_ELEMENTS[layer])
        
        # キャラクターもランダム生成
        st.session_state.character_mode = "random"
        char1 = {
            'age': random.choice(AGES),
            'job': random.choice(JOBS),
            'personality': random.choice(PERSONALITIES)
        }
        char2 = {
            'age': random.choice(AGES),
            'job': random.choice(JOBS),
            'personality': random.choice(PERSONALITIES)
        }
        st.session_state.characters = {'char1': char1, 'char2': char2}
        
        st.success("✅ 全要素をランダム生成しました！")
    
    # 個別ランダム選択
    st.subheader("🎯 個別ランダム選択")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔀 劇的状況", use_container_width=True):
            if random.random() < 0.2:
                st.session_state.elements['layer1'] = "選ばない"
            else:
                st.session_state.elements['layer1'] = random.choice(STORY_ELEMENTS['layer1'])
    
    with col2:
        if st.button("🔀 装飾・関係性", use_container_width=True):
            if random.random() < 0.2:
                st.session_state.elements['layer2'] = "選ばない"
            else:
                st.session_state.elements['layer2'] = random.choice(STORY_ELEMENTS['layer2'])

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
    
    if st.session_state.character_mode:
        st.success("✅ キャラクター設定")
    else:
        st.error("❌ キャラクター設定")

# メインコンテンツ
col1, col2 = st.columns([2, 1])

with col1:
    st.header("🎯 物語要素選択")
    
    # 選択方法の切り替え
    selection_mode = st.radio(
        "選択方法",
        ["individual", "random"],
        format_func=lambda x: "🎯 個別選択（ドロップダウン）" if x == "individual" else "🎲 ランダム選択のみ",
        horizontal=True
    )
    
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
            
            if selection_mode == "individual":
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
            
            # ランダム選択ボタン（どちらのモードでも表示）
            if st.button(f"🎯 ランダム選択", key=f"random_{layer}", use_container_width=True):
                if random.random() < 0.2:
                    st.session_state.elements[layer] = "選ばない"
                else:
                    st.session_state.elements[layer] = random.choice(STORY_ELEMENTS[layer])
            
            # 選択された要素を表示
            if st.session_state.elements[layer]:
                if st.session_state.elements[layer] == "選ばない":
                    st.markdown(f'<div class="element-box-none">この要素は使用しない</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="element-box">{st.session_state.elements[layer]}</div>', unsafe_allow_html=True)
            else:
                st.info("要素を選択してください")

with col2:
    st.header("👥 キャラクター設定")
    
    character_mode = st.radio(
        "キャラクター生成方法",
        ["random", "ai"],
        format_func=lambda x: "🎲 完全ランダム" if x == "random" else "🤖 AIがシチュエーションに応じて選択",
        key="character_mode_radio"
    )
    
    if character_mode != st.session_state.character_mode:
        st.session_state.character_mode = character_mode
        if character_mode == "random":
            char1 = {
                'age': random.choice(AGES),
                'job': random.choice(JOBS),
                'personality': random.choice(PERSONALITIES)
            }
            char2 = {
                'age': random.choice(AGES),
                'job': random.choice(JOBS),
                'personality': random.choice(PERSONALITIES)
            }
            st.session_state.characters = {'char1': char1, 'char2': char2}
    
    if st.session_state.character_mode == "random":
        # キャラクター詳細設定の選択肢
        char_detail_mode = st.radio(
            "キャラクター詳細設定",
            ["auto", "manual"],
            format_func=lambda x: "🎲 自動生成" if x == "auto" else "🎯 手動選択",
            key="char_detail_mode"
        )
        
        if char_detail_mode == "auto":
            # 自動生成モード
            if not st.session_state.characters:
                char1 = {
                    'age': random.choice(AGES),
                    'job': random.choice(JOBS),
                    'personality': random.choice(PERSONALITIES)
                }
                char2 = {
                    'age': random.choice(AGES),
                    'job': random.choice(JOBS),
                    'personality': random.choice(PERSONALITIES)
                }
                st.session_state.characters = {'char1': char1, 'char2': char2}
            
            char1 = st.session_state.characters['char1']
            char2 = st.session_state.characters['char2']
            
            st.markdown(f'''
            <div class="character-box">
            <strong>キャラクター1:</strong><br>
            {char1['age']}・{char1['job']}・{char1['personality']}な性格
            </div>
            ''', unsafe_allow_html=True)
            
            st.markdown(f'''
            <div class="character-box">
            <strong>キャラクター2:</strong><br>
            {char2['age']}・{char2['job']}・{char2['personality']}な性格
            </div>
            ''', unsafe_allow_html=True)
            
            if st.button("🔄 キャラクター再生成", use_container_width=True):
                char1 = {
                    'age': random.choice(AGES
