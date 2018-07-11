Title: [ARM] general registers
Date: 2016-05-05 05:58
Modified: 2016-05-05 05:58
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [ARM] general registers


General Registers
.................

    Name    Number      APCS Role

    a1      0           argument 1 / integer result / scratch register
    a2      1           argument 2 / scratch register
    a3      2           argument 3 / scratch register
    a4      3           argument 4 / scratch register

    v1      4           register variable
    v2      5           register variable
    v3      6           register variable
    v4      7           register variable
    v5      8           register variable

    sb/v6   9           static base / register variable
    sl/v7   10          stack limit / stack chunk handle / reg. variable
    fp      11          frame pointer
    ip      12          scratch register / new-sb in inter-link-unit calls
    sp      13          lower end of current stack frame
    lr      14          link address / scratch register
    pc      15          program counter