txt = Import["desenhista-mecanico.txt", "Text"]
pts = ToExpression @ StringReplace[
    StringSplit[StringTrim@txt, "\n"], 
    {"(" -> "{", ")" -> "}", "e" -> "*10^"}]
applyCos[x_, t_] := x[[1]] * Cos[x[[3]] * t + x[[2]]]
applySin[x_, t_] := x[[1]] * Sin[x[[3]] * t + x[[2]]]
allCos[a_] := Total[Map[applyCos[#, t] &, a]]
allSin[a_] := Total[Map[applySin[#, t] &, a]]
ParametricPlot[{allCos[pts], allSin[pts]}, {t, 0, 2 Pi}]
