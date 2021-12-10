import React from 'react'
import { PieChart, Pie, ResponsiveContainer, Cell, Tooltip, Legend } from 'recharts'
import {Card, CardGroup} from 'react-bootstrap'
export function PieChartMaha(props) {
    const data = [
    {
        sub: "Confirmed",
        skill: 25,
    },
    {
        sub: "Death",
        skill: 35,
    },
    {
        sub: "Recovered",
        skill: 15,
    },

]
const COLORS = ['rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)'];
const RADIAN = Math.PI / 180;
const renderCustomizedLabel = ({ cx, cy, midAngle, innerRadius, outerRadius, percent, index }) => {
  const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
  const x = cx + radius * Math.cos(-midAngle * RADIAN);
  const y = cy + radius * Math.sin(-midAngle * RADIAN);

  return (
    <text x={x} y={y} fill="white" textAnchor={x > cx ? 'start' : 'end'} dominantBaseline="central">
      {`${(percent * 100).toFixed(0)}%`}
    </text>
  );
}
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
  
    
            <ResponsiveContainer width="60%" aspect={2}>
                <PieChart width={450} height={450}>
                    <Pie data = {data} dataKey = "skill" nameKey = "sub" cx="50%" cy="50%" outerRadius={150} fill="#8884d8" 
                    stroke = "black" labelLine={false} label={renderCustomizedLabel}> 
                    {data.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]}
                      />))}
                      </Pie>
                    <Tooltip formatter={(value) => value + "%"} 
                    contentStyle={{fontFamily:"Poppins"}}/>
                    <Legend/>                    
                </PieChart>                
            </ResponsiveContainer>
            
        </>
    )
}