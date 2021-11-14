import useFetch from "../hooks/useFetch"
export default function Portfolio() {
    const {data, isPending, error}= useFetch('http://localhost:8000/api/portfolio/')
    console.log('init_portfoliot ....' , data)
    return (
        <div className="container">
   <div className="text-center">
      <h2 className="section-heading text-uppercase">Portfolio</h2>
      <h3 className="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
   </div>
   <div className="row">
      {!isPending  && 
      <>
      {
      data.map((item , index) =>(
      <div className="col-lg-4 col-sm-6 mb-4">
         <div className="portfolio-item">
            <a className="portfolio-link" >
               <div className="portfolio-hover">
                  <div className="portfolio-hover-content"><i className="fas fa-plus fa-3x"></i></div>
               </div>
               <img className="img-fluid" src={ item.img_url } alt="..." />
            </a>
            <div className="portfolio-caption">
               <div className="portfolio-caption-heading">{ item.name }</div>
               <div className="portfolio-caption-subheading text-muted">{ item.description }</div>
            </div>
         </div>
      </div>
      ))
      }
      </>
      }
   </div>
</div>
    )
}
