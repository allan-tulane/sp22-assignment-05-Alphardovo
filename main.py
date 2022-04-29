
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return min(MED(S[1:],T)+1, min(MED(S, T[1:])+1, MED(S[1:], T[1:])))
        else:
            return min(MED(S[1:],T)+1, min(MED(S, T[1:])+1, MED(S[1:], T[1:])+1))


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            MED[(S,T)] = min(fast_MED(S[1:],T,MED)+1, min(fast_MED(S, T[1:],MED)+1, fast_MED(S[1:], T[1:],MED)))
            return MED[(S,T)]
        else:
            MED[(S, T)] = min(fast_MED(S[1:], T, MED)+1, min(fast_MED(S, T[1:], MED) + 1, fast_MED(S[1:], T[1:], MED)+1))
            return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)][0], MED[(S, T)][1]
    if (S == ""):
        MED[(S,T)] = ("-"*len(T),T, len(T))
        # print(MED[(S,T)])
        return "-"*len(T),T
    elif (T == ""):
        MED[(S, T)] = (S, "-"*len(S), len(S))
        return S, "-"*len(S)
    else:
        if (S[0] == T[0]):
            a = fast_align_MED(S[1:], T, MED)
            b = fast_align_MED(S, T[1:], MED)
            c = fast_align_MED(S[1:], T[1:], MED)
            cnt1 = MED[(S[1:], T)][2] + 1
            cnt2 = MED[(S, T[1:])][2] + 1
            cnt3 = MED[(S[1:], T[1:])][2]
            a = (S[0]+a[0], "-"+a[1])
            b = ("-"+b[0], T[0]+b[1])
            c = (S[0]+c[0], T[0]+c[1])
            if cnt3 <= cnt2 and cnt3 <= cnt1:
                MED[(S, T)] = (c[0], c[1], cnt3)
            elif cnt2 <= cnt3 and cnt2 <= cnt1:
                MED[(S, T)] = (b[0], b[1], cnt2)
            else:
                MED[(S, T)] = (a[0], a[1], cnt1)
            return MED[(S, T)][0], MED[(S, T)][1]
        else:
            a = fast_align_MED(S[1:], T, MED)
            b = fast_align_MED(S, T[1:], MED)
            c = fast_align_MED(S[1:], T[1:], MED)
            cnt1 = MED[(S[1:], T)][2] + 1
            cnt2 = MED[(S, T[1:])][2] + 1
            cnt3 = MED[(S[1:], T[1:])][2] + 1
            a = (S[0]+a[0], "-" + a[1])
            b = ("-" + b[0], T[0]+b[1])
            c = (S[0] + c[0], T[0] + c[1])
            # if S[0] == 'u' and len(S) == len(T) + 1:
            #     print(a,b,c)
            if cnt3 <= cnt2 and cnt3 <= cnt1:
                MED[(S, T)] = (c[0], c[1], cnt3)
            elif cnt2 <= cnt3 and cnt2 <= cnt1:
                MED[(S, T)] = (b[0], b[1], cnt2)
            else:
                MED[(S, T)] = (a[0], a[1], cnt1)
            return MED[(S, T)][0], MED[(S, T)][1]

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)

def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        mst = {}
        align_S, align_T = fast_align_MED(S, T, mst)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

# test_MED()
test_align()