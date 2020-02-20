d3.csv('../static/csv/train_cleaned_2.csv').then((metadata) => {
    metadata.forEach((data)=>{
    data.SalePrice = +data.SalePrice;
    })                     
    var selection = d3.select("#gauge");
    selection.html("");

    var minPrice = d3.min(metadata, (d)=> {
        return d.SalePrice
    });
    var maxPrice = d3.max(metadata, (d)=> {
        return d.SalePrice
    });
    console.log("Min Price is " + minPrice);
    console.log("Max Price is " + maxPrice); 
    
//    d3.json("/predict").then((est_price) => {}
    
    var gauge_data = [
    {
        domain: { x: [0, 1], y: [0, 1] },
        value: 284000,
        title: { text: "Where Your Price Stand" },
        type: "indicator",
        mode: "gauge+number",
        gauge: { axis: { range: [minPrice, maxPrice] } }
    }
    ];
    
    var gauge_layout = {
        width: 640,
        height: 480,
        margin: {t:20, b:20}
    };
    
    Plotly.newPlot("gauge", gauge_data, gauge_layout);
})

