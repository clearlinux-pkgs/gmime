#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gmime
Version  : 3.0.1
Release  : 2
URL      : http://ftp.gnome.org/pub/gnome/sources/gmime/3.0/gmime-3.0.1.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/gmime/3.0/gmime-3.0.1.tar.xz
Summary  : MIME library
Group    : Development/Tools
License  : LGPL-2.1
Requires: gmime-lib
Requires: gmime-doc
Requires: gmime-data
BuildRequires : docbook-xml
BuildRequires : glib-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(libidn)
BuildRequires : pkgconfig(zlib)

%description
GMime is a set of utilities for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME)

%package data
Summary: data components for the gmime package.
Group: Data

%description data
data components for the gmime package.


%package dev
Summary: dev components for the gmime package.
Group: Development
Requires: gmime-lib
Requires: gmime-data
Provides: gmime-devel

%description dev
dev components for the gmime package.


%package doc
Summary: doc components for the gmime package.
Group: Documentation

%description doc
doc components for the gmime package.


%package lib
Summary: lib components for the gmime package.
Group: Libraries
Requires: gmime-data

%description lib
lib components for the gmime package.


%prep
%setup -q -n gmime-3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503071699
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1503071699
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GMime-3.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/gmime-3.0/gmime/gmime-application-pkcs7-mime.h
/usr/include/gmime-3.0/gmime/gmime-certificate.h
/usr/include/gmime-3.0/gmime/gmime-charset.h
/usr/include/gmime-3.0/gmime/gmime-content-type.h
/usr/include/gmime-3.0/gmime/gmime-crypto-context.h
/usr/include/gmime-3.0/gmime/gmime-data-wrapper.h
/usr/include/gmime-3.0/gmime/gmime-disposition.h
/usr/include/gmime-3.0/gmime/gmime-encodings.h
/usr/include/gmime-3.0/gmime/gmime-error.h
/usr/include/gmime-3.0/gmime/gmime-filter-basic.h
/usr/include/gmime-3.0/gmime/gmime-filter-best.h
/usr/include/gmime-3.0/gmime/gmime-filter-charset.h
/usr/include/gmime-3.0/gmime/gmime-filter-checksum.h
/usr/include/gmime-3.0/gmime/gmime-filter-dos2unix.h
/usr/include/gmime-3.0/gmime/gmime-filter-enriched.h
/usr/include/gmime-3.0/gmime/gmime-filter-from.h
/usr/include/gmime-3.0/gmime/gmime-filter-gzip.h
/usr/include/gmime-3.0/gmime/gmime-filter-html.h
/usr/include/gmime-3.0/gmime/gmime-filter-smtp-data.h
/usr/include/gmime-3.0/gmime/gmime-filter-strip.h
/usr/include/gmime-3.0/gmime/gmime-filter-unix2dos.h
/usr/include/gmime-3.0/gmime/gmime-filter-windows.h
/usr/include/gmime-3.0/gmime/gmime-filter-yenc.h
/usr/include/gmime-3.0/gmime/gmime-filter.h
/usr/include/gmime-3.0/gmime/gmime-format-options.h
/usr/include/gmime-3.0/gmime/gmime-gpg-context.h
/usr/include/gmime-3.0/gmime/gmime-header.h
/usr/include/gmime-3.0/gmime/gmime-iconv-utils.h
/usr/include/gmime-3.0/gmime/gmime-iconv.h
/usr/include/gmime-3.0/gmime/gmime-message-part.h
/usr/include/gmime-3.0/gmime/gmime-message-partial.h
/usr/include/gmime-3.0/gmime/gmime-message.h
/usr/include/gmime-3.0/gmime/gmime-multipart-encrypted.h
/usr/include/gmime-3.0/gmime/gmime-multipart-signed.h
/usr/include/gmime-3.0/gmime/gmime-multipart.h
/usr/include/gmime-3.0/gmime/gmime-object.h
/usr/include/gmime-3.0/gmime/gmime-param.h
/usr/include/gmime-3.0/gmime/gmime-parser-options.h
/usr/include/gmime-3.0/gmime/gmime-parser.h
/usr/include/gmime-3.0/gmime/gmime-part-iter.h
/usr/include/gmime-3.0/gmime/gmime-part.h
/usr/include/gmime-3.0/gmime/gmime-pkcs7-context.h
/usr/include/gmime-3.0/gmime/gmime-references.h
/usr/include/gmime-3.0/gmime/gmime-signature.h
/usr/include/gmime-3.0/gmime/gmime-stream-buffer.h
/usr/include/gmime-3.0/gmime/gmime-stream-cat.h
/usr/include/gmime-3.0/gmime/gmime-stream-file.h
/usr/include/gmime-3.0/gmime/gmime-stream-filter.h
/usr/include/gmime-3.0/gmime/gmime-stream-fs.h
/usr/include/gmime-3.0/gmime/gmime-stream-gio.h
/usr/include/gmime-3.0/gmime/gmime-stream-mem.h
/usr/include/gmime-3.0/gmime/gmime-stream-mmap.h
/usr/include/gmime-3.0/gmime/gmime-stream-null.h
/usr/include/gmime-3.0/gmime/gmime-stream-pipe.h
/usr/include/gmime-3.0/gmime/gmime-stream.h
/usr/include/gmime-3.0/gmime/gmime-text-part.h
/usr/include/gmime-3.0/gmime/gmime-utils.h
/usr/include/gmime-3.0/gmime/gmime-version.h
/usr/include/gmime-3.0/gmime/gmime.h
/usr/include/gmime-3.0/gmime/internet-address.h
/usr/lib64/libgmime-3.0.so
/usr/lib64/pkgconfig/gmime-3.0.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/gmime-3.0/CryptoContexts.html
/usr/share/gtk-doc/html/gmime-3.0/DataWrappers.html
/usr/share/gtk-doc/html/gmime-3.0/Filters.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeApplicationPkcs7Mime.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeCertificate.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeContentDisposition.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeContentType.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeCryptoContext.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeDataWrapper.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilter.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterBasic.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterBest.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterCharset.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterChecksum.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterDos2Unix.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterEnriched.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterFrom.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterGZip.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterHTML.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterSmtpData.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterStrip.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterUnix2Dos.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterWindows.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeFilterYenc.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeGpgContext.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeHeaderList.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeMessage.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeMessagePart.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeMessagePartial.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeMultipart.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeMultipartEncrypted.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeMultipartSigned.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeObject.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeParamList.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeParser.html
/usr/share/gtk-doc/html/gmime-3.0/GMimePart.html
/usr/share/gtk-doc/html/gmime-3.0/GMimePkcs7Context.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeSignature.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStream.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamBuffer.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamCat.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamFile.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamFilter.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamFs.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamGIO.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamMem.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamMmap.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamNull.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeStreamPipe.html
/usr/share/gtk-doc/html/gmime-3.0/GMimeTextPart.html
/usr/share/gtk-doc/html/gmime-3.0/Headers.html
/usr/share/gtk-doc/html/gmime-3.0/InternetAddress.html
/usr/share/gtk-doc/html/gmime-3.0/InternetAddressGroup.html
/usr/share/gtk-doc/html/gmime-3.0/InternetAddressList.html
/usr/share/gtk-doc/html/gmime-3.0/InternetAddressMailbox.html
/usr/share/gtk-doc/html/gmime-3.0/InternetAddresses.html
/usr/share/gtk-doc/html/gmime-3.0/MimeParts.html
/usr/share/gtk-doc/html/gmime-3.0/Parsers.html
/usr/share/gtk-doc/html/gmime-3.0/Streams.html
/usr/share/gtk-doc/html/gmime-3.0/ch01.html
/usr/share/gtk-doc/html/gmime-3.0/classes.html
/usr/share/gtk-doc/html/gmime-3.0/core.html
/usr/share/gtk-doc/html/gmime-3.0/fundamentals.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-3.0.devhelp2
/usr/share/gtk-doc/html/gmime-3.0/gmime-GMimeFormatOptions.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-GMimeParserOptions.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-GMimePartIter.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-GMimeReferences.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-building.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-changes-2-0.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-changes-2-2.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-changes-2-4.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-changes-2-6.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-changes-3-0.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-compiling.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-data-wrappers.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-filters.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-gmime-charset.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-gmime-encodings.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-gmime-iconv-utils.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-gmime-iconv.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-gmime-utils.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-gmime.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-question-index.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-resources.html
/usr/share/gtk-doc/html/gmime-3.0/gmime-streams.html
/usr/share/gtk-doc/html/gmime-3.0/gmime.html
/usr/share/gtk-doc/html/gmime-3.0/home.png
/usr/share/gtk-doc/html/gmime-3.0/index.html
/usr/share/gtk-doc/html/gmime-3.0/left-insensitive.png
/usr/share/gtk-doc/html/gmime-3.0/left.png
/usr/share/gtk-doc/html/gmime-3.0/right-insensitive.png
/usr/share/gtk-doc/html/gmime-3.0/right.png
/usr/share/gtk-doc/html/gmime-3.0/style.css
/usr/share/gtk-doc/html/gmime-3.0/up-insensitive.png
/usr/share/gtk-doc/html/gmime-3.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgmime-3.0.so.0
/usr/lib64/libgmime-3.0.so.0.0.1
