document.addEventListener('DOMContentLoaded', function () {
	document.querySelectorAll('.show-more').forEach(function (button) {
		button.addEventListener('click', function (event) {
			event.preventDefault()
			var shortDesc =
				this.previousElementSibling.querySelector('.short-description')
			var fullDesc =
				this.previousElementSibling.querySelector('.full-description')

			if (fullDesc.classList.contains('d-none')) {
				fullDesc.classList.remove('d-none')
				shortDesc.classList.add('d-none')
				this.textContent = 'Show less'
			} else {
				fullDesc.classList.add('d-none')
				shortDesc.classList.remove('d-none')
				this.textContent = 'Show more'
			}
		})
	})

	document.querySelectorAll('.show-comments').forEach(function (button) {
		button.addEventListener('click', function () {
			var dishId = this.getAttribute('data-dish-id')
			var commentsDiv = document.getElementById('comments-' + dishId)
			var commentsHeader = commentsDiv.previousElementSibling

			if (commentsDiv.classList.contains('d-none')) {
				commentsDiv.classList.remove('d-none')
				commentsHeader.classList.remove('d-none')
				this.textContent = 'Hide comments'
			} else {
				commentsDiv.classList.add('d-none')
				commentsHeader.classList.add('d-none')
				this.textContent = 'Show comments'
			}
		})
	})

	document.querySelectorAll('.clickable-text').forEach(function (span) {
		span.addEventListener('click', function () {
			var shortDesc =
				this.parentElement.previousElementSibling.querySelector(
					'.short-description'
				)
			var fullDesc =
				this.parentElement.previousElementSibling.querySelector(
					'.full-description'
				)

			if (fullDesc.classList.contains('d-none')) {
				fullDesc.classList.remove('d-none')
				shortDesc.classList.add('d-none')
				this.textContent = 'Show less'
			} else {
				fullDesc.classList.add('d-none')
				shortDesc.classList.remove('d-none')
				this.textContent = 'Show more'
			}
		})
	})
})
