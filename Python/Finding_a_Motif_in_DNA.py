for i from 1 to n - m do
    has_match := true
    for j from 1 to m do
        if p[j] != T[i+j] then 
            has_match := false
            break

    if has_match then output match
