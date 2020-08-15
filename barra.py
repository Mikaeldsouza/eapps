from browser import document

code = document["code"]

code.html = """<div class='bar'><a href='https://eapps.tech/'>Precisa mais alguma ferramenta maravilhosa como esta? Clique Aqui!</a></div>


<style type='text/css'>
    .bar{
    
    width:100%;color:white;text-align:center;box-sizing:border-box;padding:10px;color:white;

}

.bar a{
    color:white;
    }

@media (min-width:320px){


    font-size:50px;


}

@media (min-width:1024px){


    font-size:18px;


}
</style>

"""
