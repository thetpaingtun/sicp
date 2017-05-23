;binary search tree as set
(define (tree entry left right) (list entry left right))
(define (entry t) (car t))
(define (left t) (car (cdr t)))
(define (right t) (car (cdr (cdr t))))
(define (empty? t) (null? t))
(define (leaf entry) (tree entry nil nil))


(define (in? s v)
	(cond 
		((empty? s) False)
		((= (entry s) v) True)
		((< (entry s) v) (in? (right s) v))
		((> (entry s) v) (in? (left s) v))
	)
)


