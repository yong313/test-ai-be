from fastapi import APIRouter
from fastapi.responses import JSONResponse

apex_router = APIRouter()


# 전역 설정
GLOBAL_LEGEND = {
    "fontWeight": 700,
    "position": "bottom",
    "horizontalAlign": "center",
    "labels": {
        'colors': '#606060',
    },
    "markers": {
        "shape": "circle",
        "strokeWidth": 0.2,
        "offsetX": -5,
        "offsetY": -1,
    },
    "itemMargin": {
        "horizontal": 10,
        "vertical": 3,
    },
}

GLOBAL_DATA_LABELS = {
    "dropShadow": {
        "enabled": False
    }
}

GLOBAL_PLOT_OPTIONS = {
    "pie": {
        "donut": {
            "size": "40%"
        }
    }
}

GLOBAL_AXIS = {
    "xaxis": {
        "axisBorder": {
            "show": False
        },
        "axisTicks": {
            "show": False
        }
    },
    "yaxis": {
        "axisBorder": {
            "show": False
        },
        "axisTicks": {
            "show": False
        }
    }
}

@apex_router.get("")
async def get_apex_data():
    data = {
        "charts": [
            {
                "type": "bar",
                "options": {
                    "chart": {
                        "type": 'bar',
                        "height": 350,
                        "stacked": True,
                        "zoom": {
                            "type": 'x',
                            "enabled": True,
                            "autoScaleYaxis": True,
                        },
                        "toolbar": {
                            "autoSelected": 'zoom'
                        }
                    },
                    "dataLabels": GLOBAL_DATA_LABELS,  # 전역 dataLabels 설정 참조
                    "plotOptions": GLOBAL_PLOT_OPTIONS,  # 전역 plotOptions 설정 참조
                    "legend": GLOBAL_LEGEND,  # 전역 legend 설정 참조
                    "xaxis": GLOBAL_AXIS["xaxis"],  # 전역 xaxis 설정 참조
                    "yaxis": GLOBAL_AXIS["yaxis"],  # 전역 yaxis 설정 참조
                    "title": {"text": "일자별 상담 타입 건수 분석", "align": "left"},
                },
                "series": [
                    {"name": "업무처리", "data": [8831, 5380, 5463, 6336, 6018]},
                    {"name": "단순문의", "data": [6106, 5579, 5489, 5872, 6011]},
                    {"name": "고객불만", "data": [1518, 1221, 1112, 1155, 1132]},
                ]
            },
            {
                "type": "donut",
                "options": {
                    "chart": {"type": "pie"},
                    "title": {"text": "보험업무 별 불만족 비율"},
                    "labels": ["가입", "유지", "지급"],
                    "legend": GLOBAL_LEGEND,  # 전역 legend 설정 참조
                    "dataLabels": GLOBAL_DATA_LABELS,  # 전역 dataLabels 설정 참조
                    "plotOptions": GLOBAL_PLOT_OPTIONS,  # 전역 plotOptions 설정 참조
                    "xaxis": GLOBAL_AXIS["xaxis"],  # 전역 xaxis 설정 참조
                    "yaxis": GLOBAL_AXIS["yaxis"],  # 전역 yaxis 설정 참조
                },
                "series": [39.2, 30.8, 30.0]
            },
            {
                "type": "bar",
                "options": {
                    "chart": {
                        "type": 'bar',
                        "height": 350,
                        "stacked": True,
                        "zoom": {
                            "type": 'x',
                            "enabled": True,
                            "autoScaleYaxis": True,
                        },
                        "toolbar": {
                            "autoSelected": 'zoom'
                        }
                    },
                    "title": {"text": "연령대별 이슈 키워드 (Top 5)"},
                    "legend": GLOBAL_LEGEND,  # 전역 legend 설정 참조
                    "dataLabels": GLOBAL_DATA_LABELS,  # 전역 dataLabels 설정 참조
                    "plotOptions": GLOBAL_PLOT_OPTIONS,  # 전역 plotOptions 설정 참조
                    "xaxis": GLOBAL_AXIS["xaxis"],  # 전역 xaxis 설정 참조
                    "yaxis": GLOBAL_AXIS["yaxis"],  # 전역 yaxis 설정 참조
                },
                "series": [
                    {"name": "고객 서비스", "data": [6, 7, 14, 30, 32, 14, 2]},
                    {"name": "대출", "data": [2, 15, 28, 83, 74, 22, 2]}
                ]
            },
            {
                "type": "bar",
                "options": {
                    "chart": {"type": "bar", "stacked": True},
                    "title": {"text": "서베이 만족도 비율"},
                    "legend": GLOBAL_LEGEND,  # 전역 legend 설정 참조
                    "dataLabels": GLOBAL_DATA_LABELS,  # 전역 dataLabels 설정 참조
                    "plotOptions": GLOBAL_PLOT_OPTIONS,  # 전역 plotOptions 설정 참조
                    "xaxis": GLOBAL_AXIS["xaxis"],  # 전역 xaxis 설정 참조
                    "yaxis": GLOBAL_AXIS["yaxis"],  # 전역 yaxis 설정 참조
                },
                "series": [
                    {"name": "만족", "data": [97.47, 38.90, 93.66]},
                    {"name": "불만족", "data": [2.52, 4.02, 6.33]},
                    {"name": "미사용", "data": [0, 57.06, 0]}
                ]
            }
        ]
    }
    return JSONResponse(content=data)
