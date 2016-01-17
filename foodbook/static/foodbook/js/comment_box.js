// ReactTutorial_2.js

var data = [
	{id:1, author:"Pete Hunt", text:"This is one comment."},
	{id:2, author:"Jordan Walke", text:"This is *anooooother* comment"}

];


var Comment = React.createClass({
	/* rawMarkup is a special API that intentionally makes it difficult to insert raw HTML
	*/
	rawMarkup: function()	{		
		var rawMarkup = marked(this.props.children.toString(), {sanitize: true});
		return {__html: rawMarkup};
	},

	render: function()	{
		return(
			<div className="comment">
				<h2 className="commentAuthor">
				{this.props.author}
				</h2>
				<span dangerouslySetInnerHTML={this.rawMarkup()} />
			</div>
		);
	}
})

var CommentList = React.createClass({
	render: function()	{
		var commentNodes = this.props.data.map( function(comment)	{
			return(
				<Comment author={comment.author} key={comment.id}>
				{comment.text}
				</Comment>
				);
		});

		return (
			<div className="commentList">
				{commentNodes}
			</div>
			/*<div className = "commentList">
			<Comment author="Pete Hunt"> This is one comment</Comment>
			<Comment author="Jordan Walke">This is *another* comment</Comment>
			Hello, world! I am a commentList.
			</div>*/
		);
	}
});

var CommentForm = React.createClass({
	getInitialState: function()	{
		return{author:'', text:''};
	},
	handleAuthorChange: function(e){
		this.setState({author: e.target.value})
	},
	handleTextChange: function(e){
		this.setState({text: e.target.value})
	},
	handleSubmit: function(e) {
		e.preventDefault();
		var author = this.state.author.trim();
		var text = this.state.text.trim();
		if(!text || !author){
			return;
		}
		//TODO: send request to server
		this.props.onCommentSubmit({author: author, text: text});
		this.setState({author:'', text:''});
	},
	render: function()	{
		return (
		<form className="commentForm" onSubmit={this.handleSubmit}>
		<input
			type="text"
			placeholder="Your Name"
			value={this.state.author}
			onChange={this.handleAuthorChange}
		/>
		<input
			type="text"
			placeholder="Enter your comment"
			value={this.state.text}
			onChange={this.handleTextChange}
			/>
		<input type="submit" value="Post" />
		</form>
		)
	}
});

var CommentBox = React.createClass({
	getInitialState: function()	{
		return{data: []};
	},
	loadCommentsFromServer: function()	{
		$.ajax({
			url: this.props.url,
			dataType: 'json',
			cache: false,
			success: function(data){
				this.setState({data:data});
			}.bind(this),
		error: function(xhr,status,err)	{
			console.error(this.props.url, status, err.toString());
			}.bind(this)
		});
	},
	handleCommentSubmit: function(comment) {
		var comments = this.state.data;
		// Optimistacally set an id on the new comment. It will be replaced by an 
		// id generated by the server. In a production application you would likely
		// not use Data.now() for this and would have more robust system in place.
		
		comment.id = Date.now();
		var newComments = comments.concat([comment]);
		this.setState({data:newComments});

		$.ajax({
			url: this.props.url,
			dataType: 'json',
			type: 'POST',
			data: comment,
			success: function(data) {
				this.setState({data:comments});
			}.bind(this),
			error: function(xhr, status, err) {
				console.error(this.props.url, status, err.toString());
			}.bind(this)
		});
	},
	componentDidMount: function(){
		this.loadCommentsFromServer();
		setInterval(this.loadCommentsFromServer, this.props.pollInterval);
	},
	render: function()	{
		return (
		<div className="commentBox">			
				<h1>Comments</h1>
				<CommentList data={this.state.data}/>
				<CommentForm  onCommentSubmit={this.handleCommentSubmit} />
		</div>
		);
	}
});


ReactDOM.render(
	<CommentBox url="/api/comments" pollInterval={2000} />,
	document.getElementById('content')
);