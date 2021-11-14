import useFetch from "../hooks/useFetch"

export default function Services() {
    const {data, isPending, error}= useFetch('http://localhost:8000/api/services/')
    console.log("init_services..." , data)
    return (
        <div className="container">
   {!isPending  && 
   <div>
      <div className="text-center">
         <h2 className="section-heading text-uppercase">Services</h2>
         <h3 className="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
      </div>
      <div className="row text-center">
         {
         data.map((item , index) =>(
         <div className="col-md-4" key={item.id}>
            <span className="fa-stack fa-4x">
            <i className="fas fa-circle fa-stack-2x text-primary"></i>
            <i className={ item.class_name }></i>
            </span>
            <h4 className="my-3"> { item.product_name } </h4>
            <p className="text-muted">{ item.product_description }</p>
         </div>
         ))
         }
      </div>
   </div>
   }
</div>
    )
}
