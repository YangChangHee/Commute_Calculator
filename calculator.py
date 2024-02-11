import math
import argparse
parser = argparse.ArgumentParser()

# 실제 값
parser.add_argument("--price", type=float, default=0,required=True)
parser.add_argument("--time", type=float, default=0,required=True)
parser.add_argument("--Convenience", type=float, default=0,required=True)
parser.add_argument("--S_time", type=float, default=0,required=True)
parser.add_argument("--exception", type=float, default=0,required=True)

# 최적 점수
parser.add_argument("--optimal_price", type=float, default=0)
parser.add_argument("--optimal_time", type=float, default=21)
parser.add_argument("--optimal_Convenience", type=float, default=1)
parser.add_argument("--optimal_S_time", type=float, default=450)
parser.add_argument("--optimal_exception", type=float, default=0)

# max 점수
parser.add_argument("--max_price", type=float, default=27)
parser.add_argument("--max_time", type=float, default=59)
parser.add_argument("--max_Convenience", type=float, default=0.6)
parser.add_argument("--max_S_time", type=float, default=120)
parser.add_argument("--max_exception", type=float, default=0.05)


def custom_function(P, I, k):
    return 1 / (math.exp(abs(P - I)/k))
# 가격, 효율, 편의, 예외, 출발
custom_alpha=[0.4,0.3,0.1,0.1,0.1]

comf_table={
    "car":0.4,
    "taxi":1,
    "LG_bus":1,
    "drive_bus":1
}


if __name__ == "__main__":
    args = parser.parse_args()
    final_score= custom_alpha[0]*custom_function(args.optimal_price,args.price,args.max_price)+custom_alpha[1]*custom_function(args.optimal_time,args.time,args.max_time)+custom_alpha[2]*custom_function(args.optimal_Convenience,args.Convenience,args.max_Convenience)+\
    custom_alpha[3]*custom_function(args.optimal_S_time,args.S_time,args.S_time)+custom_alpha[4]*custom_function(args.optimal_exception,args.exception,args.max_exception)
    print(final_score)