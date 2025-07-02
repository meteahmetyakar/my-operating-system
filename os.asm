Begin Data Section

#### REGISTERS INIT START ####
#Inıt with kernel

0 0            # PC
1 200          # SP
2 0            # SYSTEM CALL RESULT
3 0            # INSTR COUNT     
4 0            # INSTRUCTION BASE
5 10999        # INSTRUCTION LIMIT
6 21           # STACK BASE
7 199          # STACK LIMIT
8 0            # DATA BASE
9 10999        # DATA LIMIT
10 0           # THREAD ID
11 0           # MODE
12 0           # TEMP PC
13 10           # HALTED THREAD COUNTER
#### REGISTERS INIT END ####


###### THREAD TABLE INIT START ######

###### ENTRY: OS ######

200 0         # threadID
201 0         # num of instruction count
202 0         # execution count
203 0         # state
204 0         # PC
205 200       # SP
206 0         # instruction base
207 10999     # instruction limit
208 21        # stack base
209 199       # stack limit
210 0         # data base  # kernel can access everywhere # data section of OS 420-999
211 10999     # data limit
212 0         # mode
213 1         # will thread schedule
214 0         # Blocked remain count
# 213-219 unused reserved

###### ENTRY END ######


###### ENTRY: THREAD-1 ######

220 1         # threadID
221 0         # num of instruction count
222 0         # execution count
223 0         # state
224 1000      # PC
225 1200      # SP
226 1000      # instruction base
227 1999      # instruction limit
228 1000      # stack base
229 1199      # stack limit
230 1200      # data base
231 1999      # data limit
232 1         # mode
233 1         # will thread schedule
234 0         # Blocked remain count
# 233-239 unused reserved

###### ENTRY END ######

###### ENTRY: THREAD-2 ######

240 2         # threadID
241 0         # num of instruction count
242 0         # execution count
243 0         # state
244 2000      # PC
245 2200      # SP
246 2000      # instruction base
247 2999      # instruction limit
248 2000      # stack base
249 2199      # stack limit
250 2200      # data base
251 2999      # data limit
252 1         # mode
253 1         # will thread schedule
254 0         # Blocked remain count
# 253-259 unused reserved

###### ENTRY END ######

###### ENTRY: THREAD-3 ######

260 3         # threadID
261 0         # num of instruction count
262 0         # execution count
263 0         # state
264 3000      # PC
265 3200      # SP
266 3000      # instruction base
267 3999      # instruction limit
268 3000      # stack base
269 3199      # stack limit
270 3200      # data base
271 3999      # data limit
272 1         # mode
273 1         # will thread schedule
274 0         # Blocked remain count
# 273-279 unused reserved

###### ENTRY END ######

###### ENTRY: THREAD-4 ######
280  4      # threadID 
281  0      # num of instruction count 
282  0      # execution count 
283  0      # state 
284  4000   # PC 
285  4200   # SP 
286  4000   # instruction base 
287  4999   # instruction limit 
288  4000   # stack base 
289  4199   # stack limit 
290  4200   # data base 
291  4999   # data limit 
292  1      # mode 
293  1      # will thread schedule 
294  0      # blocked remain count 
# 295–299 reserved

###### ENTRY: THREAD-5 ######
300  5      # threadID 
301  0      # num of instruction count 
302  0      # execution count 
303  0      # state 
304  5000   # PC 
305  5200   # SP 
306  5000   # instruction base 
307  5999   # instruction limit 
308  5000   # stack base 
309  5199   # stack limit 
310  5200   # data base 
311  5999   # data limit 
312  1      # mode 
313  1      # will thread schedule 
314  0      # blocked remain count 
# 315–319 reserved

###### ENTRY: THREAD-6 ######
320  6      # threadID 
321  0      # num of instruction count 
322  0      # execution count 
323  0      # state 
324  6000   # PC 
325  6200   # SP 
326  6000   # instruction base 
327  6999   # instruction limit 
328  6000   # stack base 
329  6199   # stack limit 
330  6200   # data base 
331  6999   # data limit 
332  1      # mode 
333  1      # will thread schedule 
334  0      # blocked remain count 
# 335–339 reserved

###### ENTRY: THREAD-7 ######
340  7      # threadID 
341  0      # num of instruction count 
342  0      # execution count 
343  0      # state 
344  7000   # PC 
345  7200   # SP 
346  7000   # instruction base 
347  7999   # instruction limit 
348  7000   # stack base 
349  7199   # stack limit 
350  7200   # data base 
351  7999   # data limit 
352  1      # mode 
353  1      # will thread schedule 
354  0      # blocked remain count 
# 355–359 reserved

###### ENTRY: THREAD-8 ######
360  8      # threadID <-- 8
361  0      # num of instruction count 
362  0      # execution count 
363  0      # state 
364  8000   # PC 
365  8200   # SP 
366  8000   # instruction base 
367  8999   # instruction limit 
368  8000   # stack base 
369  8199   # stack limit 
370  8200   # data base 
371  8999   # data limit 
372  1      # mode 
373  1      # will thread schedule 
374  0      # blocked remain count 
# 375–379 reserved

###### ENTRY: THREAD-9 ######
380  9      # threadID 
381  0      # num of instruction count 
382  0      # execution count 
383  0      # state 
384  9000   # PC 
385  9200   # SP 
386  9000   # instruction base 
387  9999   # instruction limit 
388  9000   # stack base 
389  9199   # stack limit 
390  9200   # data base 
391  9999   # data limit 
392  1      # mode 
393  1      # will thread schedule 
394  0      # blocked remain count 
# 395–399 reserved

###### ENTRY: THREAD-10 ######
400  10     # threadID 
401  0      # num of instruction count 
402  0      # execution count 
403  0      # state 
404  10000  # PC 
405  10200  # SP 
406  10000  # instruction base 
407  10999  # instruction limit 
408  10000  # stack base 
409  10199  # stack limit 
410  10200  # data base 
411  10999  # data limit 
412  1      # mode 
413  1      # will thread schedule 
414  0      # blocked remain count 
# 415–419 reserved


###### THREAD TABLE INIT END ######

# THREAD 1 INIT DATA
1210 5    # Counter
1211 0    # ZERO constant

# THREAD 2 INIT DATA
2210 10    # --> N (array size)
2211 -5    # --> key
2212 5     # --> array[0]
2213 1     # --> array[1]
2214 2     # --> array[2]
2215 6     # --> array[3]
2216 4     # --> array[4]
2217 8     # --> array[5]
2218 11    # --> array[6]
2219 15    # --> array[7]
2220 -5    # --> array[8]
2221 22    # --> array[9]

# THREAD 3 INIT DATA
3210 10    # --> N (array size)
3211 5     # --> array[0]
3212 2     # --> array[1]
3213 6     # --> array[2]
3214 8     # --> array[3]
3215 15    # --> array[4]
3216 51    # --> array[5]
3217 0     # --> array[6]
3218 3     # --> array[7]
3219 -2    # --> array[8]
3220 -1    # --> array[9]

End Data Section



Begin Instruction Section

### SCHEDULAR ### 

0 SET 10 420      # memory[420] --> threadID
1 SET 400 421     # memory[421] --> thread_entry start location
2 CPY 421 422     # memory[422] --> idx for thread table entry traverse
3 JIF 13 70       # If all threads halted, HLT the CPU

# IS THREAD HALTED
4 CPY 421 423     # get the first location of current thread's entry (400 for thread 10, 380 for thread 9 etc.) 
5 ADD 423 13      # Shift the idx
6 CPYI 423 424    # copy the location's value to memory[424]
7 JIF 424 66      # if memory[424] is 0 (so thread halted). goto 66 and schedule another thread

# IS STATE READY (READY = 0)
8 CPY 421 423     # get the first location of current thread's entry
9 ADD 423 3       # Shift the idx
10 CPYI 423 424   # copy the location's value to memory[424]
11 JIF 424 19     # if value is 0 jump the 19 and load the thread for run

# IS STATE BLOCKED (BLOCKED = 1)
12 ADD 424 -1     # substract 1 from previous 424
13 JIF 424 15     # if result is 0, this mean is thread blocked and jump 15
14 SET 18 0

15 CPY 421 430    # get the first location of current thread's entry
16 ADD 430 14     # Shift the idx, this index holds blocked remain count.
17 SUBI 3 430     # blocked remain count holds "instruction_count + 100", we substract current_instruction_count and blocked remain count
18 JIF 430 66     # if result <= 0 then jump 66 and schedule another thread because this thread still blocked 

# LOAD REGISTERS WITH THREAD ENTRY
# load registers with entry value and pass the next value

19 CPYI 422 10    # load 10th register with memory[422]
20 ADD 422 1      # pass the next value --> memory[422] = memory[422]+1

21 CPYI 422 3
22 ADD 422 1

23 ADD 422 1            
24 ADD 422 1            # pass the state

25 ADD 422 1            # pass the pc for now

26 CPYI 422 1
27 ADD 422 1

28 CPYI 422 4
29 ADD 422 1

30 CPYI 422 5
31 ADD 422 1

32 CPYI 422 6
33 ADD 422 1

34 CPYI 422 7
35 ADD 422 1

36 CPYI 422 8
37 ADD 422 1

38 CPYI 422 9
39 ADD 422 1

40 ADD 422 -8
41 USER 422

# LOAD THREAD TABLE WITH INTERRUPTED THREAD
# when an interrupt occur, pc comes here and save the current values of threads for schedule another thread
42 CPY 421 422
43 CPYI2 422 10
44 ADD 422 1

45 CPYI2 422 3
46 ADD 422 1

47 ADD 422 1            
48 ADD 422 1            # pass the state because of filled by syscall

49 ADD 422 1            # pass the pc for now

50 CPYI2 422 1
51 ADD 422 1

52 CPYI2 422 4
53 ADD 422 1

54 CPYI2 422 5
55 ADD 422 1

56 CPYI2 422 6
57 ADD 422 1

58 CPYI2 422 7
59 ADD 422 1

60 CPYI2 422 8
61 ADD 422 1

62 CPYI2 422 9
63 ADD 422 1

64 ADD 422 -8
65 CPYI2 422 12
### end load registers

66 ADD 420 -1         # decreament of threadID, this indicates the next thread that schedule
67 ADD 421 -20        # set the next thread's entry base location
68 JIF 420 0          # if 420 is 0 then goto 0th instruction. This provide circular traverse

69 SET 2 0            # if 420 is not 0 then go to 2th instruction and schedule next thread
70 HLT                # HALT CPU

# scheduling with threadID

8 CPY 421 423         # get the first location of current thread's entry
9 ADD 423 3           # Shift the idx

### SYSCALL YIELD OCCUR
#:700
700 CPY 421 425       # get the first location of current thread's entry
701 ADD 425 3         # Shift the idx (state)
702 SET 0 426   
703 CPYI2 425 426     # set the state with 0 (READY)
704 SET 42 0          # schedule another thread

### SYSCALL HLT OCCUR
#:800
800 CPY 421 425       # get the first location of current thread's entry
801 ADD 425 13        # Shift the idx (will thread schedule)
802 CPYI2 425 20      # set the location with 0. 20th register always holds 0 
803 ADD 13 -1         # 13th register holds HALTED threads, when all threads halted then cpu halted
804 SET 42 0          # schedule another thread   


### SYSCALL PRN OCCUR
#:900
900 CPY 421 425     # get the first location of current thread's entry 
901 ADD 425 3       # Shift the idx (state)
902 SET 1 426       # arr[426] = 1
903 CPYI2 425 426   # set the state with 1 (BLOCKED) 
904 CPY 3 426       # get number of instructions executed so far arr[426] = arr[3]
905 ADD 426 100     # arr[426] += 100
906 ADD 425 11      # shift the idx (blocked remain count)
907 CPYI2 425 426   # store the value
908 SET 42 0        # schedule another thread


### thread 1 ###
#:1000
1000  SET       1210 1203    # ptr_N <-- addr of N (1210)
1001  SET       0    1211    # ZERO <-- 0 (at 1211)
1002  SET       1    1202    # i <-- 1

1003  CPY       1203 1204    # tmp_ptr <-- ptr_N
1004  SUBI      1202 1204    # diff <-- i - N
1005  JIF       1204 1008    # if diff <= 0 --> goto PRINT
1006  SYSCALL   HLT          # else --> terminate thread

1008  SYSCALL   PRN  1202    # PRINT i

1009  ADD       1202 1       # i <-- i + 1
1010  JIF       1211 1003    # unconditional jump to loop start (ZERO = 0 --> always)

### thread 2 ### #LINEAR SEARCH
#:2000
2000 SET   0    2306    # ZERO <- 0
2001 SET   0    2300    # I    <- 0

2002 SET   2300 2303    # P_ptr <- I_ptr          (2303 <- 2300)
2003 SUBI  2210 2303    # P = N - I              (v1=MEM[2210]=N, ind=MEM[2303]=I, v2=MEM[I] -> MEM[2303]=N−I)
2004 JIF   2303 2021    # if (N−I) <= 0 -> NotFound

2005 SET   2212 2301    # R_X <- base_addr        (2312 is array base)
2006 SET   2300 2303    # P_ptr <- I_ptr          (2303 <- 2300)
2007 ADDI  2301 2303    # R_X = base + I          (v1=MEM[2301]=2212, ind=MEM[2303]=I, v2=MEM[I] -> MEM[2301]=2212+I)

2008 CPYI  2301 2302    # R_VAL <- MEM[R_X]       (addr=MEM[2301], val -> 2302)

2009 SET   2211 2303    # P_ptr <- KEY_ptr        (2303 <- 2211)
2010 SUBI  2302 2303    # P = R_VAL - KEY         (v1=MEM[2302]=R_VAL, ind=MEM[2303]=KEY, v2=MEM[2211]=KEY -> MEM[2303]=R_VAL−KEY)
2011 JIF   2303 2014    # if (R_VAL−KEY) <= 0 -> checkEquality
2012 ADD   2300 1       # I <- I + 1
2013 SET   2002 0       # -> MainLoop (goto 2002)

2014 SET   2302 2303    # P_ptr <- R_VAL_ptr      (2303 <- 2302)
2015 SUBI  2211 2303    # P = KEY - R_VAL         (v1=MEM[2211]=KEY, ind=MEM[2303]=R_VAL, v2=MEM[2302]=R_VAL -> MEM[2303]=KEY−R_VAL)
2016 JIF   2303 2019    # if (KEY−R_VAL) <= 0 -> Found
2017 ADD   2300 1       # I <- I + 1
2018 SET   2002 0       # -> MainLoop (goto 2002)

2019 CPY   2300 2305    # RESULT <- I
2020 SYSCALL HLT        # halt (FOUND)

2021 SET  -1   2305     # RESULT <- -1           (NotFound)
2022 SYSCALL HLT        # halt (NotFound)


### thread 3 ### #SORTING
#:3000
3000 SET 0    3238       # ZERO <- 0
3001 SET 0    3230       # I <- 0

3002 SET 3230 3232       # P_ptr <- I_ptr (3230)
3003 SUBI 3210 3232      # N - I -> MEM[3232]    (v1=MEM[3210], ind=MEM[3232]=I, v2=MEM[I] -> MEM[3232]=N-I)
3004 ADD  3232 -2        # limit2 -> MEM[3232]    (MEM[3232] += -2)
3005 CPY  3232 3239      # LMT <- limit2          (MEM[3239] <- MEM[3232])
3006 SET  3239 3233      # Q_ptr <- LMT_ptr       (MEM[3233] <- 3239)
3007 SUBI 3238 3233      # -limit2 -> MEM[3233]   (v1=MEM[3238]=0, ind=MEM[3233]=3239, v2=MEM[3239]=limit2 -> MEM[3233]=-limit2)
3008 JIF  3233 3010      # if (-limit2) <= 0 --> inner loop (3010), else continue

3009 SYSCALL   HLT
3010 SET  0    3231      # J <- 0

3011 SET  3239 3233      # Q_ptr <- LMT_ptr       (MEM[3233] <- 3239)
3012 SUBI 3231 3233      # J - LMT -> MEM[3233]   (v1=MEM[3231]=J, ind=MEM[3233]=3239, v2=MEM[3239]=limit2 -> MEM[3233]=J-limit2)
3013 JIF  3233 3016      # if (J - limit2) <= 0 --> inner body (3016), else continue
3014 ADD  3230  1        # I <- I + 1
3015 SET  3002  0        # --> outer loop (3002)

3016 SET  3211 3234      # R_X <- base_addr (3211)
3017 SET  3231 3233      # Q_ptr <- J_ptr          (MEM[3233] <- 3231)
3018 ADDI 3234 3233      # (3211 + J) -> MEM[3234] (R_X)
3019 CPY  3234 3235      # R_Y <- R_X             (MEM[3235] <- MEM[3234])
3020 ADD  3235  1        # R_Y <- R_Y + 1         (R_Y = R_X + 1)

3021 CPYI 3234 3236      # VAL_X <- MEM[R_X]
3022 CPYI 3235 3237      # VAL_Y <- MEM[R_Y]

3023 SET  3237 3232      # P_ptr <- VAL_Y_ptr     (MEM[3232] <- 3237)
3024 SUBI 3236 3232      # (VAL_X - VAL_Y) -> P   (v1=MEM[3236], ind=MEM[3232]=3237, v2=MEM[3237] -> MEM[3232]=VAL_X-VAL_Y)
3025 JIF  3232 3028      # if (VAL_X - VAL_Y) <= 0 --> skip swap (3028)
3026 CPYI2 3234 3237     # Swap -> MEM[R_X] <- VAL_Y
3027 CPYI2 3235 3236     # Swap -> MEM[R_Y] <- VAL_X

3028 ADD  3231  1        # J <- J + 1
3029 SYSCALL YIELD
3030 SET  3011  0        # --> Inner loop (3011)


### thread 4 ### 
#:4000
4000 SYSCALL HLT

### thread 5 ### 
#:5000
5000 SYSCALL HLT

### thread 6 ###
#:6000
6000 SYSCALL HLT

### thread 7 ### 
#:7000
7000 SYSCALL HLT

### thread 8 ### 
#:8000
8000 SYSCALL HLT

### thread 9 ### 
#:9000
9000 SYSCALL HLT

### thread 10 ### 
#:10000
10000 SYSCALL HLT

End Instruction Section