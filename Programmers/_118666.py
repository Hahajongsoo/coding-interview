# 성격 유형 검사하기
def solution(survey, choices):
    score_dict = {
        "R": 0,
        "T": 0,
        "F": 0,
        "C": 0,
        "M": 0,
        "J": 0,
        "A": 0,
        "N": 0,
    }

    for idx, item in enumerate(survey):
        disagree_item = item[0]
        agree_item = item[1]
        if (
            choices[idx] < 4
        ):  # choices 의 원소가 4보다 작으면 비동의에 4 - choices[i] 의 점수가 추가 # noqa: E501
            score_dict[disagree_item] += 4 - choices[idx]
        elif (
            choices[idx] > 4
        ):  # choices 의 원소가 4보다 크면 동의에 choices[i] - 4 의 점수가 추가 # noqa: E501
            score_dict[agree_item] += choices[idx] - 4

    # 둘이 같은 경우 앞의 것이 출력되므로 알파벳 순으로 인자를 넣어준다.
    answer_list = [
        max("R", "T", key=lambda x: score_dict[x]),
        max("C", "F", key=lambda x: score_dict[x]),
        max("J", "M", key=lambda x: score_dict[x]),
        max("A", "N", key=lambda x: score_dict[x]),
    ]
    answer = "".join(answer_list)
    return answer
