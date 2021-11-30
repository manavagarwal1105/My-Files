import React from 'react'
import { PieChart, Pie, ResponsiveContainer, Cell, Tooltip, Legend } from 'recharts'
export function Graph2(props) {
    const data = [
    {
        sub: "Python",
        skill: 25,
    },
    {
        sub: "  Statistics",
        skill: 35,
    },
    {
        sub: "Calculus",
        skill: 15,
    },
    {
        sub: "ReactJS",
        skill: 25,
    },
    

]
const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];
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
