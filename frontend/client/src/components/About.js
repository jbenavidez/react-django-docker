import useFetch from "../hooks/useFetch"
export default function About() {
    const {data, isPending, error}= useFetch('http://localhost:8000/api/about/')
    console.log("about init... " , data)
    return (
        <div className="container">
        <div className="text-center">
            <h2 className="section-heading text-uppercase">About</h2>
            <h3 className="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
        </div>
        <ul className="timeline">
        {!isPending  && 
                <>

{
                    data.map((item , index) =>(
                        <>
                      


                               {(() => {
                            //check is number is even or odd
                           if (item.id%2 !=0) {
                              return (
                                <li  key={item.id}  >
                                <div className="timeline-image"><img className="rounded-circle img-fluid" src={item.img_url } alt="..." /></div>
                                <div className="timeline-panel">
                                    <div className="timeline-heading">
                                        <h4> {item.date }</h4>
                                        <h4 className="subheading">{item.name }</h4>
                                    </div>
                                    <div className="timeline-body"><p className="text-muted">{item.description }</p></div>
                                </div>
                                </li>
                               )
                           }   
                           else {
                               return(
                                <li className="timeline-inverted"  key={item.id}>
                                <div className="timeline-image"><img className="rounded-circle img-fluid" src={item.img_url } alt="..." /></div>
                                <div className="timeline-panel">
                                    <div className="timeline-heading">
                                        <h4>   {item.date }</h4>
                                        <h4 className="subheading">{item.name }</h4>
                                    </div>
                                    <div className="timeline-body"><p className="text-muted">{item.description } </p></div>
                                </div>
                                </li>
                               )
                           }
                           })()}
                   

                 </>
                    ))
                    }

               
                </>
            }
          
           
            <li className="timeline-inverted">
                <div className="timeline-image">
                    <h4>
                        Be Part
                        <br />
                        Of Our
                        <br />
                        Story!
                    </h4>
                </div>
            </li>
        </ul>
    </div>
    )
}
