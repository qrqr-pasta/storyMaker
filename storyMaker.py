import streamlit as st
import random

# ページ設定
st.set_page_config(
    page_title="物語創作システム v3",
    page_icon="📚",
    layout="centered",  # モバイル対応のため変更
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
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 物語類型(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "英雄の旅(ヒーローズジャーニー)",
    "探求・クエスト",
    "下降と上昇(地獄巡りと復活)",
    "復讐譚",
    "救済・贖罪",
    "怪物退治",
    "謎解き・探偵",
    "成長・通過儀礼",
    "悲劇(破滅への道)",
    "喜劇(混沌から秩序へ)",
    "恋愛成就",
    "再生・復活",
    "放浪と帰還",
    "反乱・革命",
    "喪失と受容",
    "運命との対決",
    "立身出世",
    "犠牲と献身",
    "変身譚",
    "鏡像の物語(反転世界)",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 上位トロープ - 対立構造(15個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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
    "聖対俗",
    "記憶対忘却",
    "日常対非日常",
    "理性対本能",
    "運命対自由意志",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # キャラクター原型(15個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "探求者(未知を求める)",
    "復讐者(奪われたものを取り戻す)",
    "救済者(他者を救う使命)",
    "傍観者(巻き込まれる)",
    "トリックスター(秩序を乱す)",
    "犠牲者(選ばれし者)",
    "放浪者(居場所を探す)",
    "守護者(何かを守る)",
    "影(主人公の闇の反映)",
    "門番(試練を課す者)",
    "導師(知恵を授ける)",
    "道化(真実を笑いで語る)",
    "仲介者(異界との橋渡し)",
    "誘惑者(道を逸れさせる)",
    "二面性を持つ者(敵か味方か)",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 状況・シチュエーション(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "一つの場所から出られない(閉鎖空間)",
    "孤島に集められた人々",
    "言葉が通じない相手との対話",
    "全員が同じ夢を見る",
    "誰も信じてくれない真実",
    "祭りの一晩だけの出来事",
    "時間が止まった世界",
    "生者と死者が交わる黄昏時",
    "全員の秘密が暴かれる場",
    "役割が強制的に割り振られる",
    "現実と劇が反転する",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 禁忌・制約(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "振り返ってはならない",
    "覗いてはならない",
    "特定の部屋に入ってはならない",
    "本当の名を知ってはならない",
    "異界の食物を食べてはならない",
    "感謝を口にしてはならない",
    "触れてはいけない存在",
    "三度目は取り返しがつかない",
    "約束を破ると存在が消える",
    "血を流してはならない聖域",
    "沈黙の誓い",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 関係性の動態(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "双子の片割れ(欠けた半身)",
    "人形と人形遣い",
    "影と本体",
    "追う者と追われる者の交代",
    "救う者と救われる者の逆転",
    "忘れる者と忘れられる者",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 能力・特殊条件(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "夢に干渉する能力",
    "他者の運命を視る",
    "言葉に魔力が宿る",
    "触れたものの過去を見る",
    "死の瞬間を予知する",
    "魂を一時的に入れ替える",
    "他人の寿命を見る目",
    "嘘が物理的な形になる",
    "恐怖が具現化する体質",
    "血統による特殊能力",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 場所・空間の性質(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "橋(あちらとこちらの境界)",
    "森(迷宮、試練の場)",
    "地下・洞窟(無意識、過去)",
    "塔(隔離、監禁)",
    "廃墟(過去の残滓)",
    "劇場(虚構が現実化する場)",
    "鏡の部屋(自己との対面)",
    "井戸(異界への入口)",
    "境内・聖域(俗世から切り離された場)",
    "霧に覆われた場所(不確実性)",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 心理・認識(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     "狂気と正気の境界",
    "集団幻覚",
    "トラウマの反復",
    "抑圧された記憶の回帰",
    "解離性同一性",
    "妄想と現実の逆転",
    "観測者効果(見られることで変わる)",
    "認知の歪み",
    "偽りの記憶",
    "集合無意識の共有",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 時間・タイミング(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "運命の分岐点への回帰",
    "あと一度だけ会える機会",
    "誰かの時間を奪って生きる",
    "特定の瞬間だけ発動する力",
    "未来の自分からのメッセージ",
    "宿命からの逃走",
    "時間犯罪(時間軸への干渉)",
    "記念日の呪い",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 変化・変容(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "人間から概念へ変わる過程",
    "接触した相手に同化する",
    "二つの存在が融合していく",
    "存在形態が不安定な生命",
    "人間→動物→人間の循環",
    "老化の加速/逆行",
    "透明化/実体化",
    "性別の転換",
    "石化/彫像化",
    "脱皮/羽化(生まれ変わり)",
    "溶解と再構成",
    "分裂と増殖",
    "衣装替え(アイデンティティ変化)",
    "名前の変更/喪失による変質",
       
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 存在・実存(20個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "名前を奪われた存在",
    "概念として生きる元人間",
    "死んでいることに気づかない",
    "生きているはずのない者",
    "魂だけの存在",
    "複製された自我",
    "影だけが残った人間",
    "言葉によって定義される存在",
    "信仰によって成立する神",
    "役割に束縛された存在",
    "消えかけの存在",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 中間トロープ - 儀式・祭祀(15個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "成人の儀式(試練を経て大人に)",
    "結婚(二人が一つに)",
    "葬送(死者を送る)",
    "季節の変わり目の祭り",
    "浄化の儀式",
    "仮装/変装(別の存在になる)",
    "供物(捧げる)",
    "祈祷/呪文(言葉の力)",
    "舞踊/音楽(身体の力)",
    "火/水(浄化の媒体)",
    "生贄の選定",
    "境界を越える通過儀礼",
    "禊ぎ(穢れを落とす)",
    "契約の儀式",
    "復活祭(死と再生)",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 下位トロープ - 境界記号(10個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "橋",
    "扉/門",
    "井戸",
    "トンネル/洞窟",
    "霧",
    "カーテン/幕",
    "階段",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 下位トロープ - 変容記号(10個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "脱皮した皮",
    "蛹/繭",
    "食事(異界のものを食べる)",
    "衣装",
    "仮面",
    "髪を切る/伸ばす",
    "血",
    "涙",
    "羽根",
    "蝶",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 下位トロープ - 契約/呪い記号(10個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "鍵",
    "指輪",
    "首輪/鎖",
    "契約書",
    "印章/刻印",
    "誓約の品",
    "呪いの道具",
    "封印の札",
    "糸/縄",
    "結び目",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 下位トロープ - 知識記号(10個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "本/巻物",
    "日記",
    "手紙",
    "地図",
    "写真",
    "記録媒体",
    "禁書",
    "預言書",
    "名簿",
    "遺言",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 下位トロープ - 容器記号(10個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "箱(開けてはならないもの)",
    "瓶/壺",
    "鞄/バッグ",
    "籠",
    "棺",
    "卵",
    "袋",
    "匣",
    "宝箱",
    "封筒",
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 下位トロープ - 音/声記号(10個)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    "鈴/鐘",
    "楽器",
    "歌声",
    "呼び声",
    "囁き",
    "沈黙",
    "鳴き声",
    "足音",
    "鼓動",
    "風の音",
]

# セッション状態の初期化
if 'trope1' not in st.session_state:
    st.session_state.trope1 = None
if 'trope2' not in st.session_state:
    st.session_state.trope2 = None

# ヘッダー
st.markdown('<h1 class="main-header">📚 物語創作システム v3</h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #666; margin-bottom: 2rem;">🎲 4層トロープ統合版 - 類型・上位・中間・下位すべてをフラットに選択</div>', unsafe_allow_html=True)

# 使い方の説明
with st.expander("💡 使い方", expanded=False):
    st.markdown("""
    ### このツールの使い方
    
    1. **トロープを選択**: 左サイドバーまたは画面中央のボタンで2つのトロープをランダム選択
    2. **追加リクエスト（任意）**: 特定のキャラクター、雰囲気、長さなどを指定できます
    3. **プロンプト生成**: 「物語プロンプト生成」ボタンを押す
    4. **Claudeに送信**: 生成されたプロンプトをコピーして、[claude.ai](https://claude.ai)に貼り付ける
    5. **物語を受け取る**: Claudeが短編小説を創作します
    
    #### トロープとは？
    物語の「型」や「要素」のことです。このツールは145個のトロープから2つをランダムに組み合わせ、
    意外性のある物語の種を作ります。
    
    #### 注意事項
    - このツールはプロンプト（指示文）を生成するだけです
    - 実際の物語生成にはClaude（AI）が必要です
    - Claude.aiは無料でも使用できます
    """)

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
**指示**: 選択されたトロープに最も適した魅力的なキャラクター(1人以上)を、AIが自由に設定してください。年代、職業、性格などを物語のテーマに合わせて選択し、読者が感情移入しやすいキャラクターを作成してください。登場人物の固有名刺は重複を避けるために一般的でない特徴的な名前にしてください。特に「美咲」は頻出する傾向なので、禁止します。{request_section}

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

# 利用規約・免責事項
st.divider()
with st.expander("📜 利用規約・免責事項"):
    st.markdown("""
    ### 利用規約
    
    **1. このツールについて**
    - このツールは物語創作のためのプロンプト生成ツールです
    - 生成されたプロンプトをClaude（Anthropic社のAI）に送信することで物語が作成されます
    - このツール自体はAIを使用せず、プロンプトのテンプレートを提供するのみです
    
    **2. 著作権について**
    - 生成されたプロンプト：自由に使用・改変できます
    - AI生成された物語：Anthropic社の利用規約に従います
    - 商業利用をする場合は、[Anthropic社の利用規約](https://www.anthropic.com/legal/consumer-terms)を必ずご確認ください
    
    **3. 免責事項**
    - 生成される内容について、開発者は一切の責任を負いません
    - 不適切な内容が生成された場合、使用者の責任で対処してください
    - Claudeのコンテンツポリシーに違反する使用はおやめください
    - このツールの使用により生じたいかなる損害についても、開発者は責任を負いません
    
    **4. データの取り扱い**
    - このアプリはユーザーデータを一切保存しません
    - セッション終了後、すべての情報は自動的に削除されます
    - 外部サーバーへのデータ送信は行いません
    
    **5. その他**
    - このツールは予告なく変更・終了する場合があります
    - 本規約は予告なく変更される場合があります
    """)

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

st.markdown("""
<div style="text-align: center; color: #666; margin-top: 1rem; font-size: 0.85rem;">
    ⚠️ 生成された物語を商業利用する場合は、
    <a href="https://www.anthropic.com/legal/consumer-terms" target="_blank">Anthropicの利用規約</a>
    をご確認ください
</div>
""", unsafe_allow_html=True)
