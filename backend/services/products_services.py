import logging 

logger = logging.getLogger(__name__)

class ProductServices:

    @classmethod
    def get_product_services(self):
        """this func return a list of book"""
        book_list =  [{
                    "product_name":"E-Commerce",
                    "product_description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.",
                    "id":1,
                     "class_name":"fas fa-shopping-cart fa-stack-1x fa-inverse",
                    },
                    {
                    "product_name":"Responsive Design",
                    "product_description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.",
                    "id":2, "class_name":"fas fa-laptop fa-stack-1x fa-inverse",
                    },
                    {
                    "product_name":"Web Security",
                    "product_description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.",
                    "id":3, "class_name":"fas fa-lock fa-stack-1x fa-inverse",
                    },
                ]
        return book_list