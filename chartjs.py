from fastapi import APIRouter
from fastapi.responses import JSONResponse

chartjs_router = APIRouter()

@chartjs_router.get("")
async def get_chartjs_data():
    data = {
        "charts": [
            # Stacked Bar Chart 1
            {
                "type": "bar",
                "data": {
                    "labels": ["2024-11-11", "2024-11-12", "2024-11-13", "2024-11-14", "2024-11-15"],
                    "datasets": [
                        {
                            "label": "업무처리",
                            "data": [8831, 5380, 5463, 6336, 6018],
                            "backgroundColor": "rgba(38, 70, 83, 0.7)",
                            "borderColor": "rgba(38, 70, 83, 1)",
                            "borderWidth": 1
                        },
                        {
                            "label": "단순문의",
                            "data": [6106, 5579, 5489, 5872, 6011],
                            "backgroundColor": "rgba(42, 157, 143, 0.7)",
                            "borderColor": "rgba(42, 157, 143, 1)",
                            "borderWidth": 1
                        },
                        {
                            "label": "고객불만",
                            "data": [1518, 1221, 1112, 1155, 1132],
                            "backgroundColor": "rgba(233, 196, 106, 0.7)",
                            "borderColor": "rgba(233, 196, 106, 1)",
                            "borderWidth": 1
                        }
                    ]
                },
                "options": {
                    "responsive": True,
                    "plugins": {
                        "legend": {
                            "position": "top"
                        },
                        "title": {
                            "display": True,
                            "text": "일자별 상담 타입 건수 분석"
                        }
                    },
                    "scales": {
                        "x": {
                            "stacked": True,
                            "title": {"display": True, "text": "날짜"}
                        },
                        "y": {
                            "stacked": True,
                            "title": {"display": True, "text": "건수"}
                        }
                    }
                }
            },
            # Pie Chart
            {
                "type": "pie",
                "data": {
                    "labels": ["가입", "유지", "지급"],
                    "datasets": [
                        {
                            "data": [4.03, 5.13, 3.92],
                            "backgroundColor": [
                                "rgba(31, 119, 180, 0.8)",
                                "rgba(255, 127, 14, 0.8)",
                                "rgba(44, 160, 44, 0.8)"
                            ],
                            "hoverOffset": 4
                        }
                    ]
                },
                "options": {
                    "responsive": True,
                    "plugins": {
                        "legend": {
                            "position": "top"
                        },
                        "title": {
                            "display": True,
                            "text": "보험업무 별 불만족 비율"
                        }
                    }
                }
            },
            # Stacked Bar Chart 2
            {
                "type": "bar",
                "data": {
                    "labels": ["20대", "30대", "40대", "50대", "60대", "70대", "기타"],
                    "datasets": [
                        {
                            "label": "고객 서비스",
                            "data": [6, 30, 32, 14, 2, 0, 0],
                            "backgroundColor": "rgba(38, 70, 83, 0.7)",
                            "borderColor": "rgba(38, 70, 83, 1)",
                            "borderWidth": 1
                        },
                        {
                            "label": "대출",
                            "data": [2, 15, 28, 83, 74, 22, 2],
                            "backgroundColor": "rgba(42, 157, 143, 0.7)",
                            "borderColor": "rgba(42, 157, 143, 1)",
                            "borderWidth": 1
                        }
                    ]
                },
                "options": {
                    "responsive": True,
                    "plugins": {
                        "legend": {
                            "position": "top"
                        },
                        "title": {
                            "display": True,
                            "text": "연령대별 이슈 키워드 (Top 5)"
                        }
                    },
                    "scales": {
                        "x": {
                            "stacked": True,
                            "title": {"display": True, "text": "연령대"}
                        },
                        "y": {
                            "stacked": True,
                            "title": {"display": True, "text": "불만족 건수"}
                        }
                    }
                }
            },
            # Stacked Bar Chart 3
            {
                "type": "bar",
                "data": {
                    "labels": ["설계사 평가", "온라인 사용자 경험", "전반적인 만족도"],
                    "datasets": [
                        {
                            "label": "만족",
                            "data": [97.47, 38.90, 93.66],
                            "backgroundColor": "rgba(38, 166, 154, 0.7)",
                            "borderColor": "rgba(38, 166, 154, 1)",
                            "borderWidth": 1
                        },
                        {
                            "label": "불만족",
                            "data": [2.52, 4.02, 6.33],
                            "backgroundColor": "rgba(239, 83, 80, 0.7)",
                            "borderColor": "rgba(239, 83, 80, 1)",
                            "borderWidth": 1
                        },
                        {
                            "label": "미사용",
                            "data": [0, 57.06, 0],
                            "backgroundColor": "rgba(255, 202, 40, 0.7)",
                            "borderColor": "rgba(255, 202, 40, 1)",
                            "borderWidth": 1
                        }
                    ]
                },
                "options": {
                    "responsive": True,
                    "plugins": {
                        "legend": {
                            "position": "top"
                        },
                        "title": {
                            "display": True,
                            "text": "서베이 만족도 비율"
                        }
                    },
                    "scales": {
                        "x": {
                            "stacked": True,
                            "title": {"display": True, "text": "항목"}
                        },
                        "y": {
                            "stacked": True,
                            "title": {"display": True, "text": "비율 (%)"}
                        }
                    }
                }
            },
            
        ]
    }
    return JSONResponse(content=data)
