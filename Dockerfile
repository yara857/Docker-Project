FROM python
COPY . /ass
WORKDIR /ass
RUN pip install numpy
CMD python ass.py ker
