import logging 

logger = logging.getLogger(__name__)

class ProductServices:

    @classmethod
    def get_product_services(self):
        """this func return a list services"""
        services_list =  [{
                    "product_name":"E-Commerce",
                    "product_description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.",
                    
                     "class_name":"fas fa-shopping-cart fa-stack-1x fa-inverse",
                     "id":1,
                    },
                    {
                    "product_name":"Responsive Design",
                    "product_description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.",
                    "class_name":"fas fa-laptop fa-stack-1x fa-inverse",
                    "id":2, 
                    },
                    {
                    "product_name":"Web Security",
                    "product_description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.",
                     "class_name":"fas fa-lock fa-stack-1x fa-inverse",
                     "id":3,
                    },
                ]
        return services_list