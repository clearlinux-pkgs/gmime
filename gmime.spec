#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gmime
Version  : 3.2.0
Release  : 9
URL      : https://download.gnome.org/sources/gmime/3.2/gmime-3.2.0.tar.xz
Source0  : https://download.gnome.org/sources/gmime/3.2/gmime-3.2.0.tar.xz
Summary  : MIME library
Group    : Development/Tools
License  : LGPL-2.1
Requires: gmime-data
Requires: gmime-lib
Requires: gmime-doc
BuildRequires : docbook-xml
BuildRequires : glib-dev
BuildRequires : gnupg
BuildRequires : gobject-introspection-dev
BuildRequires : gpgme
BuildRequires : gpgme-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
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
%setup -q -n gmime-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515515838
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1515515838
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
/usr/include/gmime-3.0/gmime/gmime-autocrypt.h
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
/usr/include/gmime-3.0/gmime/gmime-filter-openpgp.h
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
/usr/share/gtk-doc/html/gmime-3.2/CryptoContexts.html
/usr/share/gtk-doc/html/gmime-3.2/DataWrappers.html
/usr/share/gtk-doc/html/gmime-3.2/Filters.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeApplicationPkcs7Mime.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeCertificate.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeContentDisposition.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeContentType.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeCryptoContext.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeDataWrapper.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilter.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterBasic.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterBest.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterCharset.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterChecksum.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterDos2Unix.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterEnriched.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterFrom.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterGZip.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterHTML.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterOpenPGP.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterSmtpData.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterStrip.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterUnix2Dos.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterWindows.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeFilterYenc.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeGpgContext.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeHeaderList.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeMessage.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeMessagePart.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeMessagePartial.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeMultipart.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeMultipartEncrypted.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeMultipartSigned.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeObject.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeParamList.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeParser.html
/usr/share/gtk-doc/html/gmime-3.2/GMimePart.html
/usr/share/gtk-doc/html/gmime-3.2/GMimePkcs7Context.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeSignature.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStream.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamBuffer.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamCat.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamFile.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamFilter.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamFs.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamGIO.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamMem.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamMmap.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamNull.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeStreamPipe.html
/usr/share/gtk-doc/html/gmime-3.2/GMimeTextPart.html
/usr/share/gtk-doc/html/gmime-3.2/Headers.html
/usr/share/gtk-doc/html/gmime-3.2/InternetAddress.html
/usr/share/gtk-doc/html/gmime-3.2/InternetAddressGroup.html
/usr/share/gtk-doc/html/gmime-3.2/InternetAddressList.html
/usr/share/gtk-doc/html/gmime-3.2/InternetAddressMailbox.html
/usr/share/gtk-doc/html/gmime-3.2/InternetAddresses.html
/usr/share/gtk-doc/html/gmime-3.2/MimeParts.html
/usr/share/gtk-doc/html/gmime-3.2/Parsers.html
/usr/share/gtk-doc/html/gmime-3.2/Streams.html
/usr/share/gtk-doc/html/gmime-3.2/ch01.html
/usr/share/gtk-doc/html/gmime-3.2/classes.html
/usr/share/gtk-doc/html/gmime-3.2/core.html
/usr/share/gtk-doc/html/gmime-3.2/fundamentals.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-3.2.devhelp2
/usr/share/gtk-doc/html/gmime-3.2/gmime-GMimeFormatOptions.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-GMimeParserOptions.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-GMimePartIter.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-GMimeReferences.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-building.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-changes-2-0.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-changes-2-2.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-changes-2-4.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-changes-2-6.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-changes-3-0.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-compiling.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-data-wrappers.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-filters.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-gmime-autocrypt.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-gmime-charset.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-gmime-encodings.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-gmime-iconv-utils.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-gmime-iconv.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-gmime-utils.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-gmime.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-question-index.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-resources.html
/usr/share/gtk-doc/html/gmime-3.2/gmime-streams.html
/usr/share/gtk-doc/html/gmime-3.2/gmime.html
/usr/share/gtk-doc/html/gmime-3.2/home.png
/usr/share/gtk-doc/html/gmime-3.2/index.html
/usr/share/gtk-doc/html/gmime-3.2/left-insensitive.png
/usr/share/gtk-doc/html/gmime-3.2/left.png
/usr/share/gtk-doc/html/gmime-3.2/right-insensitive.png
/usr/share/gtk-doc/html/gmime-3.2/right.png
/usr/share/gtk-doc/html/gmime-3.2/style.css
/usr/share/gtk-doc/html/gmime-3.2/up-insensitive.png
/usr/share/gtk-doc/html/gmime-3.2/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgmime-3.0.so.0
/usr/lib64/libgmime-3.0.so.0.200.0
