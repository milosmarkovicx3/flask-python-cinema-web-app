@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save('/var/www/uploads/uploaded_file.txt')
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
        


app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')


