//Covid tracker code, it displays one graph showing the confirmed cases of all the states


import React, { useState, useEffect } from "react";
import { Bar } from "react-chartjs-2";
import {Card, CardGroup} from 'react-bootstrap'
const Cards = () => {
    
    return (
        <>
<CardGroup>
    <Card bg='dark' text='light'>
      <Card.Body>
        <Card.Title>Infected</Card.Title>
        <Card.Text>
          Total number of COVID-19 cases.
          <br></br>
         <b></b>
        </Card.Text>
        
      </Card.Body>
      
    </Card>
    <Card bg='success' text='light'>

      <Card.Body>
        <Card.Title>Recovered</Card.Title>
        <Card.Text>
        Total number of recovered COVID-19 cases.
        
        </Card.Text>
      </Card.Body>
      
    </Card>
    <Card bg='danger' text='light'>
      
      <Card.Body>
        <Card.Title>Death</Card.Title>
        <Card.Text>
        Total number of people died due to COVID-19.
        <br></br>
         <p><b>141204</b></p>
        </Card.Text>
      </Card.Body>
      
    </Card>
  </CardGroup>
  </>
    )
    
}
const Maharashtra =() => {

    var Confirmed = []
    var Death = []
   
    const [confirmed, setConfirmed] = useState();
    const [death, setDeath] = useState();

  useEffect (async () => {
    const url = "https://covid19.mathdro.id/api/countries/India/confirmed"
    
    const response = await fetch (url);
    const datapoints = await response.json()
    
    for (const objects of datapoints) {
      Confirmed.push(objects.confirmed)
      Death.push (objects.deaths)
     }
    setConfirmed(Confirmed[0])
    setDeath(Death[0])
    
    
  }, []);
  console.log(confirmed)
  console.log(death)
    return (
        <div>
            <Cards/>
            <h3 align = 'center' style ={{fontFamily:"Patua One"}}>India Covid-19</h3>
            <br></br>
            <Bar height={100}
      data = {{
        labels:[['Confirmed'],['Death']],
        datasets:[{
          label: "Number of Cases",
                data: [confirmed,death],
                hoverBackgroundColor:'#EDC0C1',
                backgroundColor: ['red']
        }],
      }}
      options={{
        responsive:true,
        
        plugins:{
          legend:{
              display: true,
              position:'top',
              labels:{
                  font:{
                      size:14,
                      family:"Patua One"
                  }
              }
          },
          tooltip:{
              backgroundColor:'black',
              titleColor:'white',
              titleAlign:'center',
              bodyColor:'white'
          },
          
      }
      } 
      }/>
</div>
)
}

export default Maharashtra
