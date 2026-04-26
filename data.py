import time
import streamlit as st


@st.cache_data
def load_quiz_data():
    """
    퀴즈 문항 데이터를 로드합니다.

    @st.cache_data 적용 이유:
    Streamlit은 버튼 클릭, 라디오 선택 등 모든 인터랙션마다 전체 스크립트를
    처음부터 재실행합니다. 캐싱 없이는 매번 퀴즈 데이터를 새로 생성하게 되어
    불필요한 연산이 반복됩니다. @st.cache_data를 적용하면 첫 호출 결과를
    메모리에 저장하고 이후 호출에서는 저장된 값을 그대로 반환합니다.
    """
    time.sleep(0.3)  # 데이터 로드 시간 시뮬레이션 (캐싱 효과 체감용)
    questions = [
        {
            "id": 1,
            "question": "💸 월급날, 가장 먼저 하는 행동은?",
            "options": [
                "A. 통장을 보며 뿌듯해하다가 바로 쇼핑앱 켬",
                "B. 쿠팡 장바구니에 쌓아둔 것들 한 번에 결제",
                "C. 카페 가서 케이크 + 커피로 셀프 축하",
                "D. 자동이체로 저축 먼저 빠지는 거 확인하고 나머지로 생활",
            ],
            "scores": {
                "A": {"impulse": 3, "coupang": 1, "small_happy": 1, "saving": 0},
                "B": {"impulse": 1, "coupang": 3, "small_happy": 0, "saving": 0},
                "C": {"impulse": 1, "coupang": 0, "small_happy": 3, "saving": 0},
                "D": {"impulse": 0, "coupang": 0, "small_happy": 0, "saving": 3},
            },
        },
        {
            "id": 2,
            "question": "🛒 쇼핑할 때 나의 패턴은?",
            "options": [
                "A. '한정 세일'이라는 단어를 보면 일단 결제부터",
                "B. 필요한 거 하나 사러 갔다가 연관 상품 3개 추가",
                "C. 스트레스받으면 편의점/배달로 풀림",
                "D. 구매 전에 최저가 비교하고 리뷰 20개는 읽음",
            ],
            "scores": {
                "A": {"impulse": 3, "coupang": 1, "small_happy": 0, "saving": 0},
                "B": {"impulse": 0, "coupang": 3, "small_happy": 1, "saving": 0},
                "C": {"impulse": 1, "coupang": 0, "small_happy": 3, "saving": 0},
                "D": {"impulse": 0, "coupang": 0, "small_happy": 0, "saving": 3},
            },
        },
        {
            "id": 3,
            "question": "📱 카드 명세서를 봤을 때 반응은?",
            "options": [
                "A. '내가 이걸 샀나?' 싶은 항목이 절반 이상",
                "B. 로켓배송 항목이 페이지를 가득 채우고 있음",
                "C. 소액 결제가 너무 많아서 합산하기 무서움",
                "D. 예상 범위 안에서 나와서 별로 놀라지 않음",
            ],
            "scores": {
                "A": {"impulse": 3, "coupang": 1, "small_happy": 1, "saving": 0},
                "B": {"impulse": 0, "coupang": 3, "small_happy": 0, "saving": 0},
                "C": {"impulse": 1, "coupang": 0, "small_happy": 3, "saving": 0},
                "D": {"impulse": 0, "coupang": 0, "small_happy": 0, "saving": 3},
            },
        },
        {
            "id": 4,
            "question": "🏦 저축/재테크에 대한 나의 태도는?",
            "options": [
                "A. 하고 싶은데 돈이 남질 않음 (항상)",
                "B. 적금 들었다가 중도해지한 적 있음",
                "C. '소소하게 즐기는 것도 저축 아닌가'라고 생각함",
                "D. 비상금 + 적금 + 투자 계좌 따로 굴리는 중",
            ],
            "scores": {
                "A": {"impulse": 3, "coupang": 1, "small_happy": 1, "saving": 0},
                "B": {"impulse": 1, "coupang": 3, "small_happy": 0, "saving": 0},
                "C": {"impulse": 0, "coupang": 0, "small_happy": 3, "saving": 0},
                "D": {"impulse": 0, "coupang": 0, "small_happy": 0, "saving": 3},
            },
        },
        {
            "id": 5,
            "question": "😬 통장 잔액이 예상보다 적을 때 반응은?",
            "options": [
                "A. '어디서 샀더라' 기억이 안 나서 멍해짐",
                "B. 택배 상자 무덤을 보면 대충 이유를 알 것 같음",
                "C. 커피값, 배달비, 편의점이 쌓인 것 같긴 함",
                "D. 가계부 앱 열어서 어디서 초과했는지 바로 확인",
            ],
            "scores": {
                "A": {"impulse": 3, "coupang": 1, "small_happy": 1, "saving": 0},
                "B": {"impulse": 0, "coupang": 3, "small_happy": 0, "saving": 0},
                "C": {"impulse": 1, "coupang": 0, "small_happy": 3, "saving": 0},
                "D": {"impulse": 0, "coupang": 0, "small_happy": 0, "saving": 3},
            },
        },
    ]
    return questions


@st.cache_data
def load_result_data():
    """
    유형별 결과 데이터를 로드합니다.
    load_quiz_data()와 마찬가지로 @st.cache_data로 캐싱해
    반복 렌더링 시 불필요한 딕셔너리 재생성을 방지합니다.
    """
    results = {
        "impulse": {
            "emoji": "🛍️",
            "title": "소비 충동형",
            "desc": "당신의 통장은 월급이 스쳐 지나가는 환승역입니다. '한정세일', '오늘만', '마지막 재고' 같은 문구에 심장이 반응합니다. 사고 나서 후회하지만 다음 달에도 비슷한 일이 반복됩니다.",
            "tip": "💡 결제 전 10분만 멈추는 습관부터 시작하세요. 카드 저장 해제도 효과적입니다.",
        },
        "coupang": {
            "emoji": "📦",
            "title": "쿠팡 VIP형",
            "desc": "당신의 집은 이미 작은 물류센터입니다. 로켓배송 알림음이 하루의 낙이며, 장바구니는 항상 꽉 차 있습니다. 필요해서 산 건지 보여서 산 건지 경계가 흐릿합니다.",
            "tip": "💡 장바구니에 담고 24시간 뒤에 다시 보는 룰을 만들어보세요. 반절은 필요 없던 것들입니다.",
        },
        "small_happy": {
            "emoji": "🍜",
            "title": "소확행 파산형",
            "desc": "작은 행복들이 모여 큰 카드값이 됩니다. 커피 한 잔, 배달 한 번, 편의점 들르기... 각각은 소액이지만 월말에 합산하면 충격적입니다. '이 정도는 괜찮지'가 반복됩니다.",
            "tip": "💡 커피·배달·간식 각각의 월 예산을 정하고 카테고리별로 추적해보세요.",
        },
        "saving": {
            "emoji": "🐢",
            "title": "은근 절약형",
            "desc": "당신은 생각보다 통장을 잘 지키는 사람입니다. 충동 구매보다는 계획 소비에 가깝고, 명세서를 봐도 크게 당황하지 않습니다. 금융 감각이 있는 타입입니다.",
            "tip": "💡 지금처럼 하되, 남는 돈은 저축/투자 계좌로 즉시 분리해보세요. 복리가 시작됩니다.",
        },
    }
    return results