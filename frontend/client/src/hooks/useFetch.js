import { useState,useEffect } from "react";




const useFetch = (url)=>{
    const [data, setData] = useState( null);
    const [isPending, setIsPending]= useState( true);
    const [error, setError] = useState(null);

 
    useEffect( () => {
        console.log("use effect ran" ); //useeffect to get data from api, add [] as a second param to only run this function on the first render
        // to run the sjon server run the following command npx json-server --watch data/db.json --port 8000
        const abortCont = new AbortController();

        fetch(url, {signal:abortCont.signal})
              .then(res =>{
                      if(!res.ok){
                        setIsPending(false);
                       throw Error("could not fetch the data for that resources")
                      }
                      return res.json()
                    })
              .then((data)=>{
                
                setData(data);
                setIsPending(false);
                setError(null);
              })
              .catch((e) =>{
                setData([]);
                  if(e.name ==='AbortError'){
                    console.log('fetch aborted')
                  }
                  else{
                    setIsPending(false);
                    setError(e.message)
                  }
              })
                      //stop the fectch if the user click on different page 
                    return ( ) => abortCont.abort();
      },[url ]);

      return {data, isPending, error}
} 

export default useFetch; 