(define (next x)
	(+ x 1)
)


(define (abs x)
	(sqrt (square x))
)

(define (CTOF x)
	(+ 32 (* x (/ 9 5)))
)

;reurun x power to y 
(define (pow x y)
	(if (zero? y)
		1
		(* x (pow x (- y 1)))
	)
)




(define (scientific  x y)
	(if (> y 0)
		(* x (pow 10 (abs y)))
		(/ x (pow 10 (abs y)))
	)
)

(define (discount initial percent)
	(- initial (* initial (/ percent 100)))
)


(define (truediv x y)
	;only return the remainder as integer
	(floor (/ x y))

)

(define (first-digit x)
	(if (< x 10)
	x
	(first-digit (truediv x 10))
	)
)



(define (member? x lst)
   (cond  
   ((null? lst) #f)
   ((equal? x (car lst)) #t)
   (else (member? x (cdr lst)))
   
   ) 
)


(define (european-time time)
  ;return the european time. the arg passed is in the format '(8 am)
  (cond
      ((equal? (car (cdr time)) 'am) (if (< (car time) 12 ) (car time) (+ 12 (car time))))
      (else (if (< (car time) 12) (+ 12 (car time)) (car time)))
  )  
)



(define (american-time time)
   ;time is in range of 1-24
   (cond 
     ((= time 24) '(12 am))  
     ((< time 12) (list time 'am))
     ((= time 12) '(12 pm))
     (else (list (- time 12) 'pm))
   )
)




(define (teen? age)
  (and (> age 13) (< age 19))
)


(define (is-leap? y)
   (and 
      (zero? (remainder y 4))
      (or 
         (not (zero? (remainder y 100)))
         (zero? (remainder y 400))
      )
   )  
)


(define (valid-date? m d y)
   (cond 
      ((member? m '(4 6 9 11)) (and (< d 31) (> d 0)))  ;in these months should be 30 days
      ((member? m '(1 3 5 7 8 10 12)) (and (< d 32) (> d 0)))
      ((= m 2) (if (is-leap? y) (and (< d 30) (> d 0)) (and (< d 29) (> d 0))))
      (else False)
   )  
)


(define (roots a b c)
   ;return the value of x from ax2 + bx + c using quadratic formula
   (list
      (/
         (+ (- b) (sqrt (- (* b b) (* 4 a c))))  
         (* 2 a)
      )

      (/
         (- (- b) (sqrt (- (* b b) (* 4 a c))))  
         (* 2 a)
      ) 
   )
)

(define (rt a b c) 
   (let 
      (
         (discriminant (sqrt (- (* b b) (* 4 a c))))
         (minus-b (- b))
         (two-a (* 2 a))
      )
      (list (/ (+ minus-b discriminant) two-a)
            (/ (- minus-b discriminant) two-a)      
      )
   )  
)


(define (sum-square a b)
   (let 
      (
         (+ *)
         (* +)
      )
      (* (+ a a) (+ b b))
   )     
)




(define (size-of-list lst)
   (if (equal? lst '())
      0
      (+ 1 (size-of-list (cdr lst)))
   )  
)


(define (item-of-list n lst)
   (if (zero? n)
      (car lst)
      (item-of-list (- n 1) (cdr lst))
   )  
)


(define (every fn lst)
   (if (null? lst)
      lst
      (cons (fn (car lst)) (every fn (cdr lst)))
   )  
)

(define (add-three x)
   (+ x 3)  
)


;need some fix
(define (explode num)
   (if (< num 10)
      num
      (cons  (explode (truediv num 10)) (remainder num 10))
   )  
)

(define (countdown n)
   (if (= n 0)
      '(BLASTOFF)
      (cons n (countdown (- n 1)))
   )  
)

(define (copies times symbol)
   (if (zero? times)
      '()
      (cons symbol (copies (- times 1) symbol))
   ) 
)

(define (fact n)
   (if (or (= n 1) (= n 0))
      n
      (* n (fact (- n 1)))
   )
)

(define (reverse-list lst)
   (define (_reverse lst acc)
      (if (null? lst)
         acc
         (_reverse (cdr lst) (cons (car lst) acc))
      )  
   )
   (_reverse lst '())
)


(define (spell-number num)
   (define (_spell lst)
      (if (null? lst)
         '()
         (cons (spell-digit (car lst)) (_spell (cdr lst)))
      )  
   )
   (_spell (num->list num))
)

(define (spell-digit digit)
   (item-of-list digit '(zero one two three four five six seven eight nine ten))  
)

(define (remove-once symbol lst)
   (if (null? lst)
      '()
      
   )  
)

(define (keep-three-letter-words lst)
   (cond 
      ((null? lst) lst)
      ((= 3 (string-length (car lst))) (cons (car lst) (keep-three-letter-words (cdr lst))))
      (else (keep-three-letter-words (cdr lst)))
   )
)


(define  (addup lst)
   (if (null? lst)
      0
      (+ (car lst) (addup (cdr lst)))
   )  
)

(define (maxlist lst)
   (if (= 1 (length lst))
      (car lst)
      (max (car lst) (maxlist (cdr lst)))
   )  
)

(define (square-list lst)
   (if (null? lst)
      lst
      (cons (* (car lst) (car lst)) (square-list (cdr lst)))
   )  
)


(define (add-numbers lst)
   (cond 
      ((null? lst) 0)
      ((number? (car lst)) (+ (car lst) (add-numbers (cdr lst))))
      (else (add-numbers (cdr lst)))
   )  
)


(define (every-n n lst)
   (define (helper interval remaining lst)
     (cond 
      ((null? lst) lst)
      ((= 1 remaining) (cons (car lst) (helper interval interval (cdr lst))))
      (else (helper interval (- remaining 1) (cdr lst)))
     )  
   )  
    
   (helper n n lst)
  
)

(define (first-number lst)
   (cond 
      ((null? lst) "no-number")
      ((number? (car lst)) (car lst))
      (else (first-number (cdr lst)))

)
)


(define (oddth lst)
   (define (od i r lst)
      (cond 
         ((null? lst) lst)  
         ((= 1 r) (cons (car lst) (od i i (cdr lst))))
         (else (od i (- r 1) (cdr lst)))
      )  
   )

   (od 2 1 lst)
)


(define (differences lst)
   (cond 
      ((null? lst) lst) 
      ((= 1 (length lst)) '())
      (else (cons (- (car (cdr lst)) (car lst)) (differences (cdr lst))))   
      
   )  
)

(define (expand lst)
   (cond 
      ((null? lst) lst)  
      ((number? (car lst)) (cons (copies (car lst) (car (cdr lst)))) (expand (cdr lst)))
      (else (cons (car lst) (expand (cdr lst))))
   )  
)


(define (flatten seq)
   (cond 
      ((null? seq) seq)
      ((list? (car seq)) (append (flatten (car seq)) (flatten (cdr seq))))
      (else (cons (car seq) (flatten (cdr seq))))
   )  
)


(define (sorted? lst)
   (cond 
      ((null? lst) #t)
      ((= 1 (length lst)) #t)
      ((> (- (car (cdr lst)) (car lst)) -1) (sorted? (cdr lst)))
      (else #f)
   )  
  
)


(define (location sym lst)
   (define (helper count sym lst)
        (cond
            ((null? lst) #f)
            ((equal? sym (car lst)) count)
            (else (helper (+ 1 count) sym (cdr lst)))
        )  
   )
   (helper 0 sym lst)
)


(define (count-adjacent-duplicates lst)
   (define (helper lst acc)
     (cond
         ((= 1 (length lst)) acc)
         ((equal? (car lst) (cadr lst)) (helper (cdr lst) (+ 1 acc)))
         (else (helper (cdr lst) acc))
     )  
   )  
   (helper lst 0)
)

(define (remove-adjacent-duplicates lst)
   (cond 
      ((= 1 (length lst))  lst)
      ((equal? (car lst) (cadr lst)) (remove-adjacent-duplicates  (cdr lst)))
      (else (cons (car lst) (remove-adjacent-duplicates (cdr lst))))
   )  
)

(define (progressive-square? lst)
   (cond 
      ((= 1 (length lst)) #t)
      ((not (= (* (car lst) (car lst)) (cadr lst))) #f)
      (else (progressive-square? (cdr lst)))
   )  
)

(define (merge lst1 lst2)
   (cond 
      ((null? lst1) lst2)
      ((null? lst2) lst1)
      ((< (car lst1) (car lst2)) (cons (car lst1) (merge (cdr lst1) lst2)))
      ((> (car lst1) (car lst2)) (cons (car lst2) (merge lst1 (cdr lst2))))
   ) 
  
)














