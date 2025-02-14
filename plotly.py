from fastapi import APIRouter
from fastapi.responses import JSONResponse

plotly_router = APIRouter()

@plotly_router.get("")
async def get_plotly_data():
    data = {
        
            "graphs": [
                {
                    "data": [
                        {
                            "customdata": [
                                [
                                    8831,
                                    53.667578243694926
                                ],
                                [
                                    5380,
                                    44.17077175697865
                                ],
                                [
                                    5463,
                                    45.28348806366048
                                ],
                                [
                                    6336,
                                    47.41450273142259
                                ],
                                [
                                    6018,
                                    45.72600866195578
                                ]
                            ],
                            "hovertemplate": "<b>%{x}</b><br>타입: %{fullData.name}<br>-------------------<br>📞 건수: <span style='color:red'>%{customdata[0]:,}</span><br>📊 비율: <span style='color:green'>%{customdata[1]:.2f}%</span><extra></extra>",
                            "marker": {
                                "color": "#264653"
                            },
                            "name": "업무처리",
                            "x": [
                                "2024-11-11",
                                "2024-11-12",
                                "2024-11-13",
                                "2024-11-14",
                                "2024-11-15"
                            ],
                            "y": [
                                8831,
                                5380,
                                5463,
                                6336,
                                6018
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    6106,
                                    37.10726223032513
                                ],
                                [
                                    5579,
                                    45.804597701149426
                                ],
                                [
                                    5489,
                                    45.49900530503979
                                ],
                                [
                                    5872,
                                    43.942228541495176
                                ],
                                [
                                    6011,
                                    45.67282121419345
                                ]
                            ],
                            "hovertemplate": "<b>%{x}</b><br>타입: %{fullData.name}<br>-------------------<br>📞 건수: <span style='color:red'>%{customdata[0]:,}</span><br>📊 비율: <span style='color:green'>%{customdata[1]:.2f}%</span><extra></extra>",
                            "marker": {
                                "color": "#2A9D8F"
                            },
                            "name": "단순문의",
                            "x": [
                                "2024-11-11",
                                "2024-11-12",
                                "2024-11-13",
                                "2024-11-14",
                                "2024-11-15"
                            ],
                            "y": [
                                6106,
                                5579,
                                5489,
                                5872,
                                6011
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    1518,
                                    9.225159525979945
                                ],
                                [
                                    1221,
                                    10.024630541871922
                                ],
                                [
                                    1112,
                                    9.217506631299734
                                ],
                                [
                                    1155,
                                    8.643268727082242
                                ],
                                [
                                    1132,
                                    8.601170123850771
                                ]
                            ],
                            "hovertemplate": "<b>%{x}</b><br>타입: %{fullData.name}<br>-------------------<br>📞 건수: <span style='color:red'>%{customdata[0]:,}</span><br>📊 비율: <span style='color:green'>%{customdata[1]:.2f}%</span><extra></extra>",
                            "marker": {
                                "color": "#E9C46A"
                            },
                            "name": "고객불만",
                            "x": [
                                "2024-11-11",
                                "2024-11-12",
                                "2024-11-13",
                                "2024-11-14",
                                "2024-11-15"
                            ],
                            "y": [
                                1518,
                                1221,
                                1112,
                                1155,
                                1132
                            ],
                            "type": "bar"
                        }
                    ],
                    "layout": {
                        "legend": {
                            "orientation": "h",
                            "y": -0.1,
                            "x": 0.5,
                            "xanchor": "center",
                            "font": {
                                "color": "#8C9197"
                            }
                        },
                        "barmode": "stack",
                        "yaxis": {
                            "title": {
                                "text": "상담 건수"
                            },
                            "gridcolor": "#9FA3A8",
                            "linecolor": "#9FA3A8",
                            "griddash": "dot",
                            "automargin": True,
                            "zeroline": False
                        },
                        "title": {
                            "text": "일자별 상담 타입 건수 분석"
                        },
                        "xaxis": {
                            "gridcolor": "#9FA3A8",
                            "griddash": "dot",
                            "linecolor": "#9FA3A8",
                            "zeroline": False,
                            "automargin": True
                        }
                    }
                },
                {
                    "data": [
                        {
                            "hoverinfo": "text",
                            "hovertext": [
                                "<b>가입</b><br>불만족 비율: 4.03%<br>불만족 건수: 2,550<br>전체 건수: 63,232",
                                "<b>유지</b><br>불만족 비율: 5.13%<br>불만족 건수: 8,113<br>전체 건수: 158,043",
                                "<b>지급</b><br>불만족 비율: 3.92%<br>불만족 건수: 2,468<br>전체 건수: 62,970"
                            ],
                            "labels": [
                                "가입",
                                "유지",
                                "지급"
                            ],
                            "marker": {
                                "colors": [
                                    "rgba(31, 119, 180, 0.8)",
                                    "rgba(255, 127, 14, 0.8)",
                                    "rgba(44, 160, 44, 0.8)"
                                ]
                            },
                            "textinfo": "label+percent",
                            "values": [
                                4.032768218623482,
                                5.133413058471429,
                                3.9193266634905513
                            ],
                            "type": "pie"
                        }
                    ],
                    "layout": {
                        "hoverlabel": {
                            "font": {
                                "size": 12
                            },
                            "bgcolor": "white"
                        },
                        "legend": {
                            "orientation": "h",
                            "yanchor": "bottom",
                            "xanchor": "center",
                            "y": -0.2,
                            "x": 0.5,
                            "font": {
                                "color": "#8C9197"
                            }
                        },
                        "title": {
                            "text": "보험업무 별 불만족 비율"
                        },
                        "xaxis": {
                            "gridcolor": "#9FA3A8",
                            "griddash": "dot",
                            "linecolor": "#9FA3A8",
                            "zeroline": False,
                            "automargin": True
                        },
                        "yaxis": {
                            "gridcolor": "#9FA3A8",
                            "linecolor": "#9FA3A8",
                            "griddash": "dot",
                            "automargin": True,
                            "zeroline": False
                        }
                    }
                },
                {
                    "data": [
                        {
                            "customdata": [
                                [
                                    "20대",
                                    "고객 서비스 | 기타 | 고객 권리 보호",
                                    42.857142857142854,
                                    6,
                                    14
                                ],
                                [
                                    "50대",
                                    "고객 서비스 | 기타 | 고객 권리 보호",
                                    29.702970297029704,
                                    30,
                                    101
                                ],
                                [
                                    "60대",
                                    "고객 서비스 | 기타 | 고객 권리 보호",
                                    27.11864406779661,
                                    32,
                                    118
                                ],
                                [
                                    "70대",
                                    "고객 서비스 | 기타 | 고객 권리 보호",
                                    31.11111111111111,
                                    14,
                                    45
                                ],
                                [
                                    "기타",
                                    "고객 서비스 | 기타 | 고객 권리 보호",
                                    50,
                                    2,
                                    4
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "고객 서비스 | 기타 | 고객 권리 보호",
                            "x": [
                                "20대",
                                "50대",
                                "60대",
                                "70대",
                                "기타"
                            ],
                            "y": [
                                6,
                                30,
                                32,
                                14,
                                2
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "20대",
                                    "대출 | 계좌/자금 관련 | 사업 자금 대출",
                                    33.333333333333336,
                                    2,
                                    6
                                ],
                                [
                                    "40대",
                                    "대출 | 계좌/자금 관련 | 사업 자금 대출",
                                    24,
                                    6,
                                    25
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "대출 | 계좌/자금 관련 | 사업 자금 대출",
                            "x": [
                                "20대",
                                "40대"
                            ],
                            "y": [
                                2,
                                6
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "20대",
                                    "대출 | 계좌/자금 관련 | 카드 결제 문제",
                                    36.36363636363637,
                                    8,
                                    22
                                ],
                                [
                                    "30대",
                                    "대출 | 계좌/자금 관련 | 카드 결제 문제",
                                    40.54054054054054,
                                    15,
                                    37
                                ],
                                [
                                    "40대",
                                    "대출 | 계좌/자금 관련 | 카드 결제 문제",
                                    31.11111111111111,
                                    28,
                                    90
                                ],
                                [
                                    "50대",
                                    "대출 | 계좌/자금 관련 | 카드 결제 문제",
                                    44.148936170212764,
                                    83,
                                    188
                                ],
                                [
                                    "60대",
                                    "대출 | 계좌/자금 관련 | 카드 결제 문제",
                                    39.784946236559136,
                                    74,
                                    186
                                ],
                                [
                                    "70대",
                                    "대출 | 계좌/자금 관련 | 카드 결제 문제",
                                    41.509433962264154,
                                    22,
                                    53
                                ],
                                [
                                    "기타",
                                    "대출 | 계좌/자금 관련 | 카드 결제 문제",
                                    100,
                                    2,
                                    2
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "대출 | 계좌/자금 관련 | 카드 결제 문제",
                            "x": [
                                "20대",
                                "30대",
                                "40대",
                                "50대",
                                "60대",
                                "70대",
                                "기타"
                            ],
                            "y": [
                                8,
                                15,
                                28,
                                83,
                                74,
                                22,
                                2
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "20대",
                                    "대출 | 이자 관련 | 이자 관리",
                                    28.571428571428573,
                                    4,
                                    14
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "대출 | 이자 관련 | 이자 관리",
                            "x": [
                                "20대"
                            ],
                            "y": [
                                4
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "20대",
                                    "보험 | 기타 보험 관련 | 보험 적립금",
                                    36.36363636363637,
                                    4,
                                    11
                                ],
                                [
                                    "70대",
                                    "보험 | 기타 보험 관련 | 보험 적립금",
                                    24.137931034482758,
                                    7,
                                    29
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 기타 보험 관련 | 보험 적립금",
                            "x": [
                                "20대",
                                "70대"
                            ],
                            "y": [
                                4,
                                7
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "30대",
                                    "고객 서비스 | 인증/보안 | 본인 인증",
                                    18.42105263157895,
                                    7,
                                    38
                                ],
                                [
                                    "50대",
                                    "고객 서비스 | 인증/보안 | 본인 인증",
                                    17.322834645669293,
                                    22,
                                    127
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "고객 서비스 | 인증/보안 | 본인 인증",
                            "x": [
                                "30대",
                                "50대"
                            ],
                            "y": [
                                7,
                                22
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "30대",
                                    "보험 | 보험 보장 관련 | 백내장 수술 보장",
                                    18.181818181818183,
                                    6,
                                    33
                                ],
                                [
                                    "60대",
                                    "보험 | 보험 보장 관련 | 백내장 수술 보장",
                                    15.178571428571429,
                                    17,
                                    112
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 보험 보장 관련 | 백내장 수술 보장",
                            "x": [
                                "30대",
                                "60대"
                            ],
                            "y": [
                                6,
                                17
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "30대",
                                    "보험 | 보험 상품 관련 | 부부 금술 보험",
                                    16.666666666666668,
                                    5,
                                    30
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 보험 상품 관련 | 부부 금술 보험",
                            "x": [
                                "30대"
                            ],
                            "y": [
                                5
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "30대",
                                    "보험 | 보험 청구/보상/지급 관련 | 수술비 청구",
                                    24.615384615384617,
                                    16,
                                    65
                                ],
                                [
                                    "60대",
                                    "보험 | 보험 청구/보상/지급 관련 | 수술비 청구",
                                    15.283842794759826,
                                    35,
                                    229
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 보험 청구/보상/지급 관련 | 수술비 청구",
                            "x": [
                                "30대",
                                "60대"
                            ],
                            "y": [
                                16,
                                35
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "40대",
                                    "대출 | 대출 조건/상품 | 대출 기간 설정",
                                    17.94871794871795,
                                    14,
                                    78
                                ],
                                [
                                    "50대",
                                    "대출 | 대출 조건/상품 | 대출 기간 설정",
                                    17.24137931034483,
                                    20,
                                    116
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "대출 | 대출 조건/상품 | 대출 기간 설정",
                            "x": [
                                "40대",
                                "50대"
                            ],
                            "y": [
                                14,
                                20
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "40대",
                                    "보험 | 보험 보장 관련 | 도수 치료 보장",
                                    17.24137931034483,
                                    10,
                                    58
                                ],
                                [
                                    "60대",
                                    "보험 | 보험 보장 관련 | 도수 치료 보장",
                                    18.548387096774192,
                                    23,
                                    124
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 보험 보장 관련 | 도수 치료 보장",
                            "x": [
                                "40대",
                                "60대"
                            ],
                            "y": [
                                10,
                                23
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "40대",
                                    "보험 | 보험료 관련 | 보험료 재청구",
                                    17.94871794871795,
                                    7,
                                    39
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 보험료 관련 | 보험료 재청구",
                            "x": [
                                "40대"
                            ],
                            "y": [
                                7
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "50대",
                                    "보험 | 기타 보험 관련 | 보증 지급",
                                    14.545454545454545,
                                    16,
                                    110
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 기타 보험 관련 | 보증 지급",
                            "x": [
                                "50대"
                            ],
                            "y": [
                                16
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "70대",
                                    "보험 | 보험 보장 관련 | 치과 치료 보장",
                                    18.91891891891892,
                                    7,
                                    37
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 보험 보장 관련 | 치과 치료 보장",
                            "x": [
                                "70대"
                            ],
                            "y": [
                                7
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "70대",
                                    "보험 | 보험료 관련 | 보험료 출금 문제",
                                    21.73913043478261,
                                    5,
                                    23
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 보험료 관련 | 보험료 출금 문제",
                            "x": [
                                "70대"
                            ],
                            "y": [
                                5
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "기타",
                                    "보험 | 기타 보험 관련 | 입원 및 통원 치료",
                                    100,
                                    1,
                                    1
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 기타 보험 관련 | 입원 및 통원 치료",
                            "x": [
                                "기타"
                            ],
                            "y": [
                                1
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "기타",
                                    "보험 | 기타 보험 관련 | 조직 검사 결과",
                                    50,
                                    1,
                                    2
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 기타 보험 관련 | 조직 검사 결과",
                            "x": [
                                "기타"
                            ],
                            "y": [
                                1
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    "기타",
                                    "보험 | 보험 계약 관련 | 계약자 정보 확인",
                                    50,
                                    1,
                                    2
                                ]
                            ],
                            "hovertemplate": "<b>연령대: %{customdata[0]}</b><br><b>태그: %{customdata[1]}</b><br>--------------------------------<br>불만족 비율: <span style='color:green'>%{customdata[2]:.2f}%</span><br>불만족 건수: <span style='color:red'>%{customdata[3]:,}</span><br>전체 건수: <span style='color:blue'>%{customdata[4]:,}</span><br><extra></extra>",
                            "name": "보험 | 보험 계약 관련 | 계약자 정보 확인",
                            "x": [
                                "기타"
                            ],
                            "y": [
                                1
                            ],
                            "type": "bar"
                        }
                    ],
                    "layout": {
                        "margin": {
                            "l": 20,
                            "r": 20,
                            "t": 40,
                            "b": 80
                        },
                        "xaxis": {
                            "title": {
                                "text": "연령대"
                            },
                            "categoryorder": "array",
                            "categoryarray": [
                                "20대",
                                "30대",
                                "40대",
                                "50대",
                                "60대",
                                "70대",
                                "기타"
                            ],
                            "gridcolor": "#9FA3A8",
                            "griddash": "dot",
                            "linecolor": "#9FA3A8",
                            "zeroline": False,
                            "automargin": True
                        },
                        "title": {
                            "text": "연령대별 이슈 키워드 (Top 5)"
                        },
                        "yaxis": {
                            "title": {
                                "text": "불만족 건수"
                            },
                            "gridcolor": "#9FA3A8",
                            "linecolor": "#9FA3A8",
                            "griddash": "dot",
                            "automargin": True,
                            "zeroline": False
                        },
                        "barmode": "stack",
                        "hovermode": "closest",
                        "showlegend": False,
                        "legend": {
                            "font": {
                                "color": "#8C9197"
                            }
                        }
                    }
                },
                {
                    "data": [
                        {
                            "customdata": [
                                [
                                    1428,
                                    97.47440273037543
                                ],
                                [
                                    2868,
                                    38.90396093326099
                                ],
                                [
                                    7036,
                                    93.66347177848775
                                ]
                            ],
                            "hovertemplate": "<b>%{x}</b><br>만족도: 만족<br>건수: %{customdata[0]}<br>비율: %{customdata[1]:.2f}%<extra></extra>",
                            "name": "만족",
                            "x": [
                                "설계사 평가",
                                "온라인 사용자 경험",
                                "전반적인 만족도"
                            ],
                            "y": [
                                97.47440273037543,
                                38.90396093326099,
                                93.66347177848775
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    37,
                                    2.525597269624573
                                ],
                                [
                                    297,
                                    4.028757460661964
                                ],
                                [
                                    476,
                                    6.336528221512247
                                ]
                            ],
                            "hovertemplate": "<b>%{x}</b><br>만족도: 불만족<br>건수: %{customdata[0]}<br>비율: %{customdata[1]:.2f}%<extra></extra>",
                            "name": "불만족",
                            "x": [
                                "설계사 평가",
                                "온라인 사용자 경험",
                                "전반적인 만족도"
                            ],
                            "y": [
                                2.525597269624573,
                                4.028757460661964,
                                6.336528221512247
                            ],
                            "type": "bar"
                        },
                        {
                            "customdata": [
                                [
                                    0,
                                    0
                                ],
                                [
                                    4207,
                                    57.067281606077046
                                ],
                                [
                                    0,
                                    0
                                ]
                            ],
                            "hovertemplate": "<b>%{x}</b><br>만족도: 미사용<br>건수: %{customdata[0]}<br>비율: %{customdata[1]:.2f}%<extra></extra>",
                            "name": "미사용",
                            "x": [
                                "설계사 평가",
                                "온라인 사용자 경험",
                                "전반적인 만족도"
                            ],
                            "y": [
                                0,
                                57.067281606077046,
                                0
                            ],
                            "type": "bar"
                        }
                    ],
                    "layout": {
                        "legend": {
                            "orientation": "h",
                            "y": -0.1,
                            "x": 0.5,
                            "xanchor": "center",
                            "font": {
                                "color": "#8C9197"
                            }
                        },
                        "xaxis": {
                            "categoryorder": "array",
                            "categoryarray": [
                                "전반적인 만족도",
                                "설계사 평가",
                                "온라인 사용자 경험"
                            ],
                            "gridcolor": "#9FA3A8",
                            "griddash": "dot",
                            "linecolor": "#9FA3A8",
                            "zeroline": False,
                            "automargin": True
                        },
                        "title": {
                            "text": "서베이 만족도 비율"
                        },
                        "yaxis": {
                            "title": {
                                "text": "비율 (%)"
                            },
                            "gridcolor": "#9FA3A8",
                            "linecolor": "#9FA3A8",
                            "griddash": "dot",
                            "automargin": True,
                            "zeroline": False
                        },
                        "barmode": "stack"
                    }
                }
            ]
        }
    
    return JSONResponse(content=data)