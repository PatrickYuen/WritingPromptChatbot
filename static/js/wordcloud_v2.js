function wordCloud(selector) {

    var fill = d3.scale.category20();

    //Construct the word cloud's SVG element
    var svg = d3.select(selector).append("svg")
        .attr("width", 300)
        .attr("height", 300)
        .append("g")
        .attr("transform", "translate(150,150)");


    //Draw the word cloud
    function draw(words) {
        var cloud = svg.selectAll("g text")
                        .data(words, function(d) { return d.text; })

        //Entering words
        cloud.enter()
            .append("text")
            .style("font-family", "Impact")
            .style("fill", function(d, i) { return fill(i); })
            .attr("text-anchor", "middle")
            .attr('font-size', 1)
            .text(function(d) { return d.text; });

        //Entering and existing words
        cloud
            .transition()
                .duration(600)
                .style("font-size", function(d) { return d.size + "px"; })
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .style("fill-opacity", 1);

        //Exiting words
        cloud.exit()
            .transition()
                .duration(200)
                .style('fill-opacity', 1e-6)
                .attr('font-size', 1)
                .remove();
    }


    //Use the module pattern to encapsulate the visualisation code. We'll
    // expose only the parts that need to be public.
    return {

        //Recompute the word cloud for a new set of words. This method will
        // asycnhronously call draw when the layout has been computed.
        //The outside world will need to call this function, so make it part
        // of the wordCloud return value.
        update: function(words) {
            d3.layout.cloud().size([300, 300])
                .words(words)
                .rotate(function() { return ~~(Math.random() * 2) * 90; })
                .font("Impact")
                .fontSize(function(d) { return d.size; })
                .on("end", draw)
                .start();
        }
    }

}

function updatePrompts(recPrompts) {
	$('#PromptList').hide().fadeOut( 1500, function() {
		$('#PromptList').remove();
		
		var ul = $("<ul id=\"PromptList\" class=\"text-left\" style=\"margin-top:20px;padding-left:5px;overflow:hidden;\">" );
		// iterate over the array and build the list
		for (var i = 0; i < recPrompts.length; ++i) {
			ul.append("<li style=\"margin:5px;\">" + recPrompts[i] + "</li>");
		}
		
		$( "#RecPrompts" ).append(ul);
		ul.hide().fadeIn( 800 );
	});
}

//This method tells the word cloud to redraw with a new set of words.
//In reality the new words would probably come from a server request,
// user input or some other source.
function showNewWords(vis) {
	$.ajax({
		url: '/getData',
		type: 'GET',
		success: function(response) {
			
			//Update Recent Prompts
			updatePrompts(JSON.parse(response).rp_output)
			
			//Update WordCloud
			vis.update(JSON.parse(response).wc_output)
			setTimeout(function() { showNewWords(vis) }, 5000)
		},
		error: function(error) {
			console.log(error);
		}
	});
}

//Create a new instance of the word cloud visualisation.
var myWordCloud = wordCloud('#WordCloud');

//Start cycling through the demo data
showNewWords(myWordCloud);