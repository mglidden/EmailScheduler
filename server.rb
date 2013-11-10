require 'sinatra'

get '/' do
  erb :index
end

post '/update' do
  updated_schedule = params[:schedule]
  File.open('schedule.txt', 'w') { |file|
    file.write(updated_schedule)
  }
  'Updated schedule.'
end
