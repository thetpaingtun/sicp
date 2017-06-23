;from chapter 15 to 


(define (sort  lst)
   ;selecton sort
   (cond 
      ((null? lst) lst)
      ((= 1 (length lst)) lst)
      (else 
      (let 
         (
            (smallest (find-smallest lst))
         )   
         (cons smallest (sort (remove-once smallest lst)))
      )
      )
    )   
   
)

(define (find-smallest lst)
   (cond 
      ((null? (cdr lst)) (symbol->string (car lst)))
      ((string<? (symbol->string (car lst)) (find-smallest (cdr lst))) (symbol->string (car lst)))
      (else (find-smallest (cdr lst)))
   )  
)

(define (remove-once s lst)
   (cond 
      ((null? lst) lst)  
      ((string=? s (symbol->string (car lst))) (cdr lst))
      (else (cons (car lst) (remove-once s (cdr lst))))
   )
)















