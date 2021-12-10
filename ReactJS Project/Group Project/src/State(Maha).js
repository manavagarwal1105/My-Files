import React, { Component } from 'react'

import Maharashtra from './Graph1(Maharashtra)'
import Button from 'react-bootstrap/Button'
import { PieChartMaha } from './PieChart(Maha)'
import { PieChart } from 'recharts'

export default class State extends Component {
    constructor(props) {
        super(props)
        
        this.state = {
                 data: ""
        }

    }
    
    show = () =>{ 
        this.setState({
            data: <div style ={{fontFamily:"Poppins",color:"white"}}>
                <h2 style={{fontFamily:"Poppins", fontSize:"20px",color:"black"}}><b>&nbsp;<u>Bar Graph</u></b></h2>
            <Maharashtra/>
            </div>
     
        })
    }

    show2 = () =>{ 
        this.setState({
            data: <div style ={{fontFamily:"Poppins",color:"white"}}>
                <h2 style={{fontFamily:"Poppins", fontSize:"20px",color:"black"}}><b>&nbsp;<u>Pie Chart: </u></b></h2>
                <PieChartMaha/>
            </div>
     
        })
    }
    
     
        


    render() {
        return (
            <>
            <br></br>
            <div style={{textAlign : "center"}}>
            <h2 style={{fontFamily:"Poppins", fontSize:"20px",color:"black"}}><b>&nbsp;<u>Choose the type of graph:-  </u></b></h2>
            
            &nbsp;<Button variant = "danger" type = "button" onClick = {this.show} style={{fontFamily:"Poppins"}}>Bar Chart</Button> &nbsp;
            <Button variant = "danger" type = "button" onClick = {this.show2} style={{fontFamily:"Poppins"}}>Pie Chart</Button> &nbsp;
            
            </div>
            {this.state.data}
            </>
        )
        
    }
}
