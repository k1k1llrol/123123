import click
import tqdm
import requests

@click.command()
@click.option('--url', default='https://raw.githubusercontent.com/k1k1llrol/123/blob/main/main.py', help='URL to download file from')
@click.option('--output', 'output_file', required=True, help='File to save the downloaded content to')
def download_file(url, output_file):
    total_size = 0
    with requests.get(url, stream=True) as r:
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm.tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(output_file, 'wb') as f:
            for data in r.iter_content(block_size):
                f.write(data)
                progress_bar.update(block_size)
        progress_bar.close()
    print(f"Downloaded {total_size}iB to {output_file}")

@click.command()
def greet():
    click.echo("Takker!")

def main():
    greet()
    download_file()

if __name__ == '__main__':
    main()